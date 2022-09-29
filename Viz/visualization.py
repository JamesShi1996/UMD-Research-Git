
import recom_gender
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys


matplotlib.rc('xtick', labelsize=6)
matplotlib.rc('ytick', labelsize=5)


from ng_viz_fields import *


#########################################

## global config
total_participants = 220
invalid_proportion = 0.1
# error acceptance
error_acceptance = 0.2

#########################################



def simple_distribution():


    plt.subplot(451)
    plt.bar(Kick_a_ball_names, Kick_a_ball_values)

    temp = Kick_a_ball_names
    temp = [e.replace(" ", "_") for e in temp]

    Kick_a_ball_zip = dict(zip(temp,Kick_a_ball_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Kick_a_ball_zip)
    Kick_a_ball_values_predict = []

    for key, value in expected_value.items():
        Kick_a_ball_values_predict.append(value)

    y_pos = np.arange(len(Kick_a_ball_names))
    plt.bar(y_pos, Kick_a_ball_values_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Kick_a_ball_names)

    plt.title('Kick a ball')




    plt.subplot(452)
    plt.bar(Stomp_out_fire_names, Stomp_out_fire_values)

    temp = Stomp_out_fire_names
    temp = [e.replace(" ", "_") for e in temp]

    Stomp_out_fire_zip = dict(zip(temp, Stomp_out_fire_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Stomp_out_fire_zip)
    Stomp_out_fire_values_predict = []

    for key, value in expected_value.items():
        Stomp_out_fire_values_predict.append(value)

    y_pos = np.arange(len(Stomp_out_fire_names))
    plt.bar(y_pos, Stomp_out_fire_values_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Stomp_out_fire_names)

    plt.title('Stomp out fire')




    plt.subplot(453)
    plt.bar(Draw_a_circle_names, Draw_a_circle_values)

    temp = Draw_a_circle_names
    temp = [e.replace(" ", "_") for e in temp]

    Draw_a_circle_zip = dict(zip(temp, Draw_a_circle_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Draw_a_circle_zip)
    Draw_a_circle_predict = []

    for key, value in expected_value.items():
        Draw_a_circle_predict.append(value)

    y_pos = np.arange(len(Draw_a_circle_names))
    plt.bar(y_pos, Draw_a_circle_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Draw_a_circle_names)
    plt.title('Draw a circle')

    # mark: option N/A is not included

    plt.subplot(454)
    plt.bar(Dominant_Leg_names, Dominant_Leg_values)
    temp = Dominant_Leg_names
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Dominant_Leg_zip = dict(zip(temp, Dominant_Leg_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Dominant_Leg_zip)
    Dominant_Leg_predict = []

    for key, value in expected_value.items():
        Dominant_Leg_predict.append(value)

    y_pos = np.arange(len(Dominant_Leg_names))
    plt.bar(y_pos, Dominant_Leg_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Dominant_Leg_names)
    plt.title('Dominant Leg')

    plt.subplot(455)
    plt.bar(Age_names, Age_values)
    temp = Age_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Age_zip = dict(zip(temp, Age_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Age_zip)
    Age_predict = []

    for key, value in expected_value.items():
        Age_predict.append(value)

    y_pos = np.arange(len(Age_names))
    plt.bar(y_pos, Age_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Age_names)
    plt.title('Age')


    plt.subplot(456)
    plt.bar(Gender_names, Gender_values)
    temp = Gender_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Gender_zip = dict(zip(temp, Gender_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Gender_zip)
    Gender_predict = []

    for key, value in expected_value.items():
        Gender_predict.append(value)

    y_pos = np.arange(len(Gender_names))
    plt.bar(y_pos, Gender_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Gender_names)
    plt.title('Gender')


    plt.subplot(457)
    plt.bar(Race_names, Race_values)
    temp = Race_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Race_zip = dict(zip(temp, Race_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Race_zip)
    Race_predict = []

    for key, value in expected_value.items():
        Race_predict.append(value)

    y_pos = np.arange(len(Race_names))
    plt.bar(y_pos, Race_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Race_names)
    plt.title('Race')



    plt.subplot(458)
    plt.bar(Dominant_Hand_names, Dominant_Hand_values)
    temp = Dominant_Hand_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Dominant_Hand_zip = dict(zip(temp, Dominant_Hand_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Dominant_Hand_zip)
    Dominant_Hand_predict = []

    for key, value in expected_value.items():
        Dominant_Hand_predict.append(value)

    y_pos = np.arange(len(Dominant_Hand_names))
    plt.bar(y_pos, Dominant_Hand_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Dominant_Hand_names)
    plt.title('Dominant Hand')



    plt.subplot(459)
    plt.bar(Watch_sports_regularly_names, Watch_sports_regularly_values)
    temp = Watch_sports_regularly_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Watch_sports_regularly_zip = dict(zip(temp, Watch_sports_regularly_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Watch_sports_regularly_zip)
    Watch_sports_regularly_predict = []

    for key, value in expected_value.items():
        Watch_sports_regularly_predict.append(value)

    y_pos = np.arange(len(Watch_sports_regularly_names))
    plt.bar(y_pos, Watch_sports_regularly_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Watch_sports_regularly_names)
    plt.title('Watch sports regularly')


    plt.subplot(4, 5, 10)
    plt.bar(Sports_growup_or_last5year_names, Sports_growup_or_last5year_values)
    temp = Sports_growup_or_last5year_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Sports_growup_or_last5year_zip = dict(zip(temp, Sports_growup_or_last5year_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Sports_growup_or_last5year_zip)
    Sports_growup_or_last5year_predict = []

    for key, value in expected_value.items():
        Sports_growup_or_last5year_predict.append(value)

    y_pos = np.arange(len(Sports_growup_or_last5year_names))
    plt.bar(y_pos, Sports_growup_or_last5year_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Sports_growup_or_last5year_names)
    plt.title('Sports growing up(in 5 years)')


    plt.subplot(4, 5, 11)
    plt.bar(Education_names, Education_values)
    temp = Education_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Education_zip = dict(zip(temp, Education_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Education_zip)
    Education_predict = []

    for key, value in expected_value.items():
        Education_predict.append(value)

    y_pos = np.arange(len(Education_names))
    plt.bar(y_pos, Education_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Education_names)
    plt.title('Education')


    plt.subplot(4, 5, 12)
    plt.bar(Job_with_3D_names, Job_with_3D_values)
    temp = Job_with_3D_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Job_with_3D_zip = dict(zip(temp, Job_with_3D_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Job_with_3D_zip)
    Job_with_3D_predict = []

    for key, value in expected_value.items():
        Job_with_3D_predict.append(value)

    y_pos = np.arange(len(Job_with_3D_names))
    plt.bar(y_pos, Job_with_3D_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Job_with_3D_names)
    plt.title('Job with 3D visual')



    plt.subplot(4, 5, 13)
    plt.bar(Infront_of_computer_names, Infront_of_computer_values)
    temp = Infront_of_computer_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    Infront_of_computer_zip = dict(zip(temp, Infront_of_computer_values))

    expected_value = recom_gender.have_sample(total_participants, 0, Infront_of_computer_zip)
    Infront_of_computer_predict = []

    for key, value in expected_value.items():
        Infront_of_computer_predict.append(value)

    y_pos = np.arange(len(Infront_of_computer_names))
    plt.bar(y_pos, Infront_of_computer_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, Infront_of_computer_names)
    plt.title('Infront of computer')



    plt.subplot(4, 5, 14)
    plt.bar(written_oral_mediums_names, written_oral_mediums_values)
    temp = written_oral_mediums_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    written_oral_mediums_zip = dict(zip(temp, written_oral_mediums_values))

    expected_value = recom_gender.have_sample(total_participants, 0, written_oral_mediums_zip)
    written_oral_mediums_predict = []

    for key, value in expected_value.items():
        written_oral_mediums_predict.append(value)

    y_pos = np.arange(len(written_oral_mediums_names))
    plt.bar(y_pos, written_oral_mediums_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, written_oral_mediums_names)
    plt.title('written oral mediums')



    plt.subplot(4, 5, 15)
    plt.bar(flown_a_drone_names, flown_a_drone_values)
    temp = flown_a_drone_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    flown_a_drone_zip = dict(zip(temp, flown_a_drone_values))

    expected_value = recom_gender.have_sample(total_participants, 0, flown_a_drone_zip)
    flown_a_drone_predict = []

    for key, value in expected_value.items():
        flown_a_drone_predict.append(value)

    y_pos = np.arange(len(flown_a_drone_names))
    plt.bar(y_pos, flown_a_drone_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, flown_a_drone_names)
    plt.title('flown a drone')



    plt.subplot(4, 5, 16)
    plt.bar(control_robot_names, control_robot_values)
    temp = control_robot_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    control_robot_zip = dict(zip(temp, control_robot_values))

    expected_value = recom_gender.have_sample(total_participants, 0, control_robot_zip)
    control_robot_predict = []

    for key, value in expected_value.items():
        control_robot_predict.append(value)

    y_pos = np.arange(len(control_robot_names))
    plt.bar(y_pos, control_robot_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, control_robot_names)
    plt.title('control robot')



    plt.subplot(4, 5, 17)
    plt.bar(often_playgame_names, often_playgame_values)
    temp = often_playgame_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    often_playgame_zip = dict(zip(temp, often_playgame_values))

    expected_value = recom_gender.have_sample(total_participants, 0, often_playgame_zip)
    often_playgame_predict = []

    for key, value in expected_value.items():
        often_playgame_predict.append(value)

    y_pos = np.arange(len(often_playgame_names))
    plt.bar(y_pos, often_playgame_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, often_playgame_names)
    plt.title('often play games')



    plt.subplot(4, 5, 18)
    plt.bar(game_controller_names, game_controller_values)
    temp = game_controller_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    game_controller_zip = dict(zip(temp, game_controller_values))

    expected_value = recom_gender.have_sample(total_participants, 0, game_controller_zip)
    game_controller_predict = []

    for key, value in expected_value.items():
        game_controller_predict.append(value)

    y_pos = np.arange(len(game_controller_names))
    plt.bar(y_pos, game_controller_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, game_controller_names)
    plt.title('game controller')



    plt.subplot(4, 5, 19)
    plt.bar(type_of_game_names, type_of_game_values)
    plt.title('type of game')
    temp = type_of_game_names
    temp = [e.replace(" ", "_") for e in temp]
    temp = [e.replace("-", "_") for e in temp]
    temp = [e.replace("/", "_") for e in temp]

    type_of_game_zip = dict(zip(temp, type_of_game_values))

    expected_value = recom_gender.have_sample(total_participants, 0, type_of_game_zip)
    type_of_game_predict = []

    for key, value in expected_value.items():
        type_of_game_predict.append(value)

    y_pos = np.arange(len(type_of_game_names))
    plt.bar(y_pos, type_of_game_predict, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
    plt.xticks(y_pos, type_of_game_names)

    plt.suptitle('One question one plot, # of entries = {}'.format(Race.count()))
    plt.show()



def computer_two_variables(arg1, arg2):

    All_variables = df.iloc[:, :]

    arg1_retrieved = All_variables[arg1]
    arg2_retrieved = All_variables[arg2]

    arg1_names = get_argument_names(arg1_retrieved)
    arg2_names = get_argument_names(arg2_retrieved)

    I = pd.Index(arg1_names)
    C = pd.Index(arg2_names)
    temp_df = pd.DataFrame(data=np.zeros((len(arg1_names), len(arg2_names))), index=I, columns=C)

    # grp1 is DataFrameGroupBy
    grp1 = df.groupby([arg1, arg2])

    # series1 is a series
    series1 = grp1[arg2].size()

    # stack1 is a dataframe
    stack1 = series1.unstack()

    # combine data from temp DataFrame and current dataframe(which has value from excel)

    temp_df.loc[stack1.index, stack1.columns] = stack1

    temp_data = temp_df.fillna(0)


    # reverse the data_frame with columns and rows
    temp_data = temp_data.T

    temp_dic = temp_data.to_dict()

    # print(temp_dic)

    arg1_retrieved = All_variables[arg1]
    arg2_retrieved = All_variables[arg2]

    arg1_names = get_argument_names(arg1_retrieved)

    arg2_names = get_argument_names(arg2_retrieved)
    arg2_values = get_argument_values(arg2_retrieved)

    arg2_zip_final = dict(zip(arg2_names, arg2_values))

    arg2_names = [e.replace(" ", "_") for e in arg2_names]
    arg2_names = [e.replace("-", "_") for e in arg2_names]
    arg2_names = [e.replace("/", "_") for e in arg2_names]

    temp_total_values = []
    temp_keys = []

    for x, y in temp_dic.items():
        temp_keys.append(x)
        temp_types = []
        temp_values = []
        for i, o in y.items():
            temp_types.append(i)
            temp_values.append(o)
        temp_total_values.append(temp_values)

    # # plot two variable compare graph
    fig1 = temp_data.plot(kind='bar', figsize=(10, 6), title="{}   VS.  {}".format(arg1, arg2))

    plt.show()


def computer_two_variables_with_predict(arg1, arg2):

    arg1_retrieved = All_variables[arg1]
    arg2_retrieved = All_variables[arg2]

    arg1_names = get_argument_names(arg1_retrieved)
    arg2_names = get_argument_names(arg2_retrieved)

    # temp DataFrame with all 0
    I = pd.Index(arg1_names)
    C = pd.Index(arg2_names)
    temp_df = pd.DataFrame(data=np.zeros((len(arg1_names), len(arg2_names))), index=I, columns=C)

    # grp1 is DataFrameGroupBy
    grp1 = df.groupby([arg1, arg2])

    # series1 is a series
    series1 = grp1[arg2].size()

    # stack1 is a data_frame
    stack1 = series1.unstack()
    # print(stack1)

    # combine data from temp DataFrame and current data_frame(which has value from excel)
    temp_df.loc[stack1.index, stack1.columns] = stack1

    temp_data = temp_df.fillna(0)

    # reverse the data_frame with columns and rows
    temp_data = temp_data.T

    temp_dic = temp_data.to_dict()

    arg1_retrieved = All_variables[arg1]
    arg2_retrieved = All_variables[arg2]

    arg1_names = get_argument_names(arg1_retrieved)

    arg2_names = get_argument_names(arg2_retrieved)
    arg2_values = get_argument_values(arg2_retrieved)

    arg2_zip_final = dict(zip(arg2_names, arg2_values))

    arg2_names = [e.replace(" ", "_") for e in arg2_names]
    arg2_names = [e.replace("-", "_") for e in arg2_names]
    arg2_names = [e.replace("/", "_") for e in arg2_names]

    arg2_zip = dict(zip(arg2_names, arg2_values))

    temp_total_values = []
    temp_keys = []

    for x,y in temp_dic.items():
        temp_keys.append(x)
        temp_types = []
        temp_values = []
        for i,o in y.items():
            temp_types.append(i)
            temp_values.append(o)
        temp_total_values.append(temp_values)


    # reduce proportion of field like: N/A, Prefer not to say, etc.
    invalid_field = 0

    for col in temp_df.columns:
        if(col == "Prefer not to say" or col == "N/A" or col == "Prefer not to answer"):
            invalid_field += 1

    arg1_size = len(arg1_names)
    arg2_size = len(arg2_names)
    invalid_field_value = round((invalid_proportion*total_participants*invalid_field)/(arg1_size), 1)

    arg_proportion = round(((total_participants-invalid_field_value)/(arg2_size - invalid_field))/(arg1_size), 1)

    alter = True

    for col in temp_df.columns:
        if(col == "Prefer not to say" or col == "N/A" or col == "Prefer not to answer"):
            temp_df[col].values[:] = invalid_field_value
        else:
            if(alter):
                temp_df[col].values[:] = arg_proportion + error_acceptance
                alter = False
            else:
                temp_df[col].values[:] = arg_proportion - error_acceptance
                alter = True

    temp_df = temp_df.T

    ax = temp_df.plot(kind='bar', figsize=(10, 6), title="{}   VS.  {}".format(arg1, arg2), color="xkcd:beige")
    ax.get_legend().remove()

    temp_data.plot(kind='bar', figsize=(10, 6), title="{}   VS.  {}".format(arg1, arg2), ax=ax)

    plt.show()


def get_argument_values(arg):
    if arg.equals(Kick_a_ball):
        return Kick_a_ball_values
    elif arg.equals(Stomp_out_fire):
        return Stomp_out_fire_values
    elif arg.equals(Draw_a_circle):
        return Draw_a_circle_values
    elif arg.equals(Dominant_Leg):
        return Dominant_Leg_values
    elif arg.equals(Age):
        return Age_values
    elif arg.equals(Gender):
        return Gender_values
    elif arg.equals(Race):
        return Race_values
    elif arg.equals(Dominant_Hand):
        return Dominant_Hand_values
    elif arg.equals(Watch_sports_regularly):
        return Watch_sports_regularly_values
    elif arg.equals(Sports_growup_or_last5year):
        return Sports_growup_or_last5year_values
    elif arg.equals(Education):
        return Education_values
    elif arg.equals(Job_with_3D):
        return Job_with_3D_values
    elif arg.equals(Infront_of_computer):
        return Infront_of_computer_values
    elif arg.equals(written_oral_mediums):
        return written_oral_mediums_values
    elif arg.equals(flown_a_drone):
        return flown_a_drone_values
    elif arg.equals(control_robot):
        return control_robot_values
    elif arg.equals(often_playgame):
        return often_playgame_values
    elif arg.equals(game_controller):
        return game_controller_values
    elif arg.equals(type_of_game):
        return type_of_game_values


def get_argument_names(arg):

    if arg.equals(Kick_a_ball):
        return Kick_a_ball_names
    elif arg.equals(Stomp_out_fire):
        return Stomp_out_fire_names
    elif arg.equals(Draw_a_circle):
        return Draw_a_circle_names
    elif arg.equals(Dominant_Leg):
        return Dominant_Leg_names
    elif arg.equals(Age):
        return Age_names
    elif arg.equals(Gender):
        return Gender_names
    elif arg.equals(Race):
        return Race_names
    elif arg.equals(Dominant_Hand):
        return Dominant_Hand_names
    elif arg.equals(Watch_sports_regularly):
        return Watch_sports_regularly_names
    elif arg.equals(Sports_growup_or_last5year):
        return Sports_growup_or_last5year_names
    elif arg.equals(Education):
        return Education_names
    elif arg.equals(Job_with_3D):
        return Job_with_3D_names
    elif arg.equals(Infront_of_computer):
        return Infront_of_computer_names
    elif arg.equals(written_oral_mediums):
        return written_oral_mediums_names
    elif arg.equals(flown_a_drone):
        return flown_a_drone_names
    elif arg.equals(control_robot):
        return control_robot_names
    elif arg.equals(often_playgame):
        return often_playgame_names
    elif arg.equals(game_controller):
        return game_controller_names
    elif arg.equals(type_of_game):
        return type_of_game_names
    else:
        print("false argument")


def main():

    simple_distribution()


if __name__ == '__main__':
    main()
