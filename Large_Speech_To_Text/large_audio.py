# coding=utf-8
# Import libraries
from builtins import list
import random
import json
import string
from pydub import AudioSegment
import io
import os
from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1 import enums
from google.cloud.speech_v1p1beta1 import types
import wave
from google.cloud import storage




# initial settings
#####################################

#setting up file path and output path
filepath = "/Users/SJW/Desktop/Research/Large_Speech_To_Text/input/"  # Input audio file path
output_filepath = "/Users/SJW/Desktop/Research/Large_Speech_To_Text/output/"  # Final transcript path

# assign the .json file you generated for credential here

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "c-key.json"

# put the bucket name that you created here
bucket_name_here = 'test-bucket-sjw'



#####################################






# stereo to mono convert
def stereo_to_mono(audio_name):
    sound = AudioSegment.from_wav(audio_name)
    sound = sound.set_channels(1)
    sound.export(audio_name, format="wav")


# identify the video frame rate and channel numbers
# if channel is > 1, then it is not mono audio.
# use stereo_to_mono to convert
def frame_rate_channel(audio_name):
    with wave.open(audio_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        return frame_rate, channels


# upload the audio to the google cloud with specific bucket
def upload_to_blob(bucket_name, source_file_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_file_name)

    blob.upload_from_filename(source_file_name)


# delete the file from google cloud if need
def delete_from_blob(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()


# timeout option.
# It is the number of seconds that the transcribe function
# will actively transcribe a current audio file.
# You can adjust this setting to a larger number
# if the audio file seconds is larger than the number provided here.

def Speech_To_Text(audio_name):
    # The name of the audio file to transcribe
    file_name = filepath + audio_name


    frame_rate, channels = frame_rate_channel(file_name)

    # convert audio file to mono if it is not
    if channels > 1:
        stereo_to_mono(file_name)


    bucket_name = bucket_name_here
    source_file_name = filepath + audio_name
    destination_file_name = audio_name

    upload_to_blob(bucket_name, source_file_name, destination_file_name)


    gcs_uri_here = 'gs://' + bucket_name_here + '/'

    gcs_uri = gcs_uri_here + audio_name

    transcript = ''

    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)

    # configuration
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=frame_rate,
        language_code='en-US',
        # add punctuation config
        enable_automatic_punctuation=True,
        # add timestamp config
        enable_word_time_offsets=True
        )

    print('Waiting for operation to complete...' + '\n')


    # Detects speech in the audio file
    operation = client.long_running_recognize(config, audio)
    response = operation.result(timeout=10000)

    transcript = ""

    data = {}
    data_only_caption = []

    for result in response.results:


        words_info = result.alternatives[0].words

        first_word = list(words_info)[0]
        last_word = list(words_info)[-1]

        # random pure digits
        # hash = random.getrandbits(64)


        # random letters and digits
        hash = randomStringDigits(8)

        start_t = first_word.start_time.seconds + first_word.start_time.nanos/1000000000.0

        end_t = last_word.end_time.seconds + last_word.end_time.nanos/1000000000.0


        data[hash] = []

        words = []

        for word in words_info:
            word_start_t = word.start_time.seconds + word.start_time.nanos/1000000000.0
            word_end_t = word.end_time.seconds + word.end_time.nanos/1000000000.0
            words.append({
                "word: " : word.word,
                "start time: " : word_start_t,
                "end time: " : word_end_t
            })


        data[hash].append({
            "type: " : "speech",
            "transcript: " : result.alternatives[0].transcript,
            "Start time (seconds): " : start_t,
            "End time (seconds): " : end_t,
            "Words: " : words
        })

        # Only return whole caption without any extra info
        data_only_caption.append(result.alternatives[0].transcript)



    delete_from_blob(bucket_name, destination_file_name)

    #return data
    return data_only_caption



# generating random letters and digits
def randomStringDigits(stringLength=6):

    lettersAndDigits = string.ascii_letters + string.digits

    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


# get rid of hidden files that start with .
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

# write out the final script.
def write_transcript(data, output_filename):
    outfile = output_filepath + output_filename
    with open(outfile, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    # f = open(output_filepath + output_filename, "w+")
    # f.write(transcript)
    # f.close()


# can convert single or multiple audio file into single or multiple json file
# put all the audio file into "filepath" directory and it will transcript all
# and out put to output_filepath

if __name__ == "__main__":
    for audio_name in listdir_nohidden(filepath):
        print('\n' + "File Processing: " + audio_name + '\n')
        # check if already has output json file
        exists = os.path.isfile(output_filepath + audio_name.split('.')[0] + '.json')
        if exists:
            print("File Already Existed: " + audio_name + '\n')
            pass
        else:
            data = Speech_To_Text(audio_name)
            output_filename = audio_name.split('.')[0] + '.json'
            write_transcript(data, output_filename)
            print("Completed: " + output_filename + '\n')










############ extra information and method

# command to turn wav file to mono .flac file ：
# ffmpeg -i test1.wav -ac 1 -ab 48k test1mono.flac
