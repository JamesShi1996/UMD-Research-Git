
import pandas as pd



xl = pd.ExcelFile("Demographic Questions Form this one.xlsx")



global df
df = xl.parse("Demographic Questions Form")

All_variables = df.iloc[:, :]


Kick_a_ball = All_variables['Kick a ball as far as possible']


Stomp_out_fire = All_variables['Stomp out fire on the floor']
Draw_a_circle = All_variables['Draw a circle']
Dominant_Leg = All_variables['Dominant Leg']
Age = All_variables['Age']
Gender = All_variables['Gender']
Race = All_variables['Race']


# not clearly categorical data
Country_grow_up = All_variables['In which country did you spend the most time growing up?']
Country_last5year = All_variables['In which country did you spend the most time in the last 5 years?']

Dominant_Hand = All_variables['Dominant Hand']
Watch_sports_regularly = All_variables['Do you watch sports regularly?']
Sports_growup_or_last5year = All_variables['Did you play sports growing up, or play sports in the past 5 years?']
Education = All_variables['My education/ training/ certifications are in']
Job_with_3D = All_variables['Does your job entail dealing with 3D visualizations?']
Infront_of_computer = All_variables['Do you work in front of a computer more than 1 hour at a time?']
written_oral_mediums = All_variables[
    'Do you communicate with other using written and oral mediums more than 1 hour per day?']
flown_a_drone = All_variables['Have you ever flown a drone/ RC helicopters/ RC planes?']
control_robot = All_variables['Have you controlled/ navigated a robot or heavy machinery before?']
often_playgame = All_variables['How often do you play video games?']
game_controller = All_variables['What types of game controllers have you used? Select all that apply.']
type_of_game = All_variables['What are the types of games you play? Select all that apply.']




Kick_a_ball_count = Kick_a_ball.value_counts()
Kick_a_ball_count_left = 0 if (Kick_a_ball_count.get("Kick with left leg") == None) else Kick_a_ball_count[
    "Kick with left leg"]
Kick_a_ball_count_right = 0 if (Kick_a_ball_count.get("Kick with right leg") == None) else Kick_a_ball_count[
    "Kick with right leg"]
Kick_a_ball_count_either = 0 if (Kick_a_ball_count.get("Kick with either leg") == None) else Kick_a_ball_count[
    "Kick with either leg"]

# global Kick_a_ball_names, Kick_a_ball_values
Kick_a_ball_names = ['Kick with left leg', 'Kick with right leg', 'Kick with either leg']
Kick_a_ball_values = [Kick_a_ball_count_left, Kick_a_ball_count_right, Kick_a_ball_count_either]





Stomp_out_fire_count = Stomp_out_fire.value_counts()
Stomp_out_fire_count_left = 0 if (Stomp_out_fire_count.get("Stomp with left leg") == None) else \
    Stomp_out_fire_count["Stomp with left leg"]
Stomp_out_fire_count_right = 0 if (Stomp_out_fire_count.get("Stomp with right leg") == None) else \
    Stomp_out_fire_count["Stomp with right leg"]
Stomp_out_fire_count_either = 0 if (Stomp_out_fire_count.get("Stomp with either leg") == None) else \
    Stomp_out_fire_count["Stomp with either leg"]
Stomp_out_fire_count_both = 0 if (Stomp_out_fire_count.get("Stomp with both legs") == None) else \
    Stomp_out_fire_count["Stomp with both legs"]
# global Stomp_out_fire_names, Stomp_out_fire_values
Stomp_out_fire_names = ['Stomp with left leg', 'Stomp with right leg', 'Stomp with either leg',
                        'Stomp with both legs']
Stomp_out_fire_values = [Stomp_out_fire_count_left, Stomp_out_fire_count_right, Stomp_out_fire_count_either,
                         Stomp_out_fire_count_both]



Kick_a_ball_count = Kick_a_ball.value_counts()
Kick_a_ball_count_left = 0 if (Kick_a_ball_count.get("Kick with left leg") == None) else Kick_a_ball_count[
    "Kick with left leg"]
Kick_a_ball_count_right = 0 if (Kick_a_ball_count.get("Kick with right leg") == None) else Kick_a_ball_count[
    "Kick with right leg"]
Kick_a_ball_count_either = 0 if (Kick_a_ball_count.get("Kick with either leg") == None) else Kick_a_ball_count[
    "Kick with either leg"]


Kick_a_ball_names = ['Kick with left leg', 'Kick with right leg', 'Kick with either leg']
Kick_a_ball_values = [Kick_a_ball_count_left, Kick_a_ball_count_right, Kick_a_ball_count_either]


Stomp_out_fire_count = Stomp_out_fire.value_counts()
Stomp_out_fire_count_left = 0 if (Stomp_out_fire_count.get("Stomp with left leg") == None) else \
    Stomp_out_fire_count["Stomp with left leg"]
Stomp_out_fire_count_right = 0 if (Stomp_out_fire_count.get("Stomp with right leg") == None) else \
    Stomp_out_fire_count["Stomp with right leg"]
Stomp_out_fire_count_either = 0 if (Stomp_out_fire_count.get("Stomp with either leg") == None) else \
    Stomp_out_fire_count["Stomp with either leg"]
Stomp_out_fire_count_both = 0 if (Stomp_out_fire_count.get("Stomp with both legs") == None) else \
    Stomp_out_fire_count["Stomp with both legs"]
# global Stomp_out_fire_names, Stomp_out_fire_values
Stomp_out_fire_names = ['Stomp with left leg', 'Stomp with right leg', 'Stomp with either leg',
                        'Stomp with both legs']
Stomp_out_fire_values = [Stomp_out_fire_count_left, Stomp_out_fire_count_right, Stomp_out_fire_count_either,
                         Stomp_out_fire_count_both]



Draw_a_circle_count = Draw_a_circle.value_counts()
Draw_a_circle_count_left = 0 if (Draw_a_circle_count.get("Draw with left leg") == None) else Draw_a_circle_count[
    "Draw with left leg"]
Draw_a_circle_count_right = 0 if (Draw_a_circle_count.get("Draw with right leg") == None) else Draw_a_circle_count[
    "Draw with right leg"]
Draw_a_circle_count_either = 0 if (Draw_a_circle_count.get("Draw with either leg") == None) else \
    Draw_a_circle_count["Draw with either leg"]

# global Draw_a_circle_names, Draw_a_circle_values
Draw_a_circle_names = ['Draw with left leg', 'Draw with right leg', 'Draw with either leg']
Draw_a_circle_values = [Draw_a_circle_count_left, Draw_a_circle_count_right, Draw_a_circle_count_either]



Dominant_Leg_count = Dominant_Leg.value_counts()
Dominant_Leg_count_left = 0 if (Dominant_Leg_count.get("Left-Legged") == None) else Dominant_Leg_count[
    "Left-Legged"]
Dominant_Leg_count_right = 0 if (Dominant_Leg_count.get("Right-Legged") == None) else Dominant_Leg_count[
    "Right-Legged"]
Dominant_Leg_count_ambi = 0 if (Dominant_Leg_count.get("Ambi-Legged") == None) else Dominant_Leg_count[
    "Ambi-Legged"]
Dominant_Leg_count_cross = 0 if (Dominant_Leg_count.get("Cross-Dominant") == None) else Dominant_Leg_count[
    "Cross-Dominant"]
Dominant_Leg_count_na = 0 if (Dominant_Leg_count.get("N/A") == None) else Dominant_Leg_count[
    "N/A"]

# global Dominant_Leg_names, Dominant_Leg_values
Dominant_Leg_names = ['Right-Legged', 'Left-Legged', 'Ambi-Legged', 'Cross-Dominant', 'N/A']
Dominant_Leg_values = [Dominant_Leg_count_left, Dominant_Leg_count_right, Dominant_Leg_count_ambi,
                       Dominant_Leg_count_cross, Dominant_Leg_count_na]



Age_count = Age.value_counts()
Age_count_under_17 = 0 if (Age_count.get("17 or under") == None) else Age_count["17 or under"]
Age_count_18_24 = 0 if (Age_count.get("18-24") == None) else Age_count["18-24"]
Age_count_25_34 = 0 if (Age_count.get("25-34") == None) else Age_count["25-34"]
Age_count_35_44 = 0 if (Age_count.get("35-44") == None) else Age_count["35-44"]
Age_count_45_54 = 0 if (Age_count.get("45-54") == None) else Age_count["45-54"]
Age_count_55_64 = 0 if (Age_count.get("55-64") == None) else Age_count["55-64"]
Age_count_65_older = 0 if (Age_count.get("65 or older") == None) else Age_count["65 or older"]
Age_count_prefer_no = 0 if (Age_count.get("Prefer not to answer") == None) else Age_count["Prefer not to answer"]

# global Age_names, Age_values
Age_names = ['17 or under', '18-24', '25-34', '35-44', '45-54', '55-64', '65 or older', 'Prefer not to answer']
Age_values = [Age_count_under_17, Age_count_18_24, Age_count_25_34, Age_count_35_44, Age_count_45_54,
              Age_count_55_64, Age_count_65_older, Age_count_prefer_no]



Gender_count = Gender.value_counts()
Gender_count_male = 0 if (Gender_count.get("Male") == None) else Gender_count["Male"]
Gender_count_female = 0 if (Gender_count.get("Female") == None) else Gender_count["Female"]
Gender_count_prefer_no = 0 if (Gender_count.get("Prefer not to say") == None) else Gender_count["Prefer not to say"]

Gender_names = ['Male', 'Female', 'Prefer not to say']
Gender_values = [Gender_count_male, Gender_count_female, Gender_count_prefer_no]



Race_count = Race.value_counts()
Race_count_asian_pacific = 0 if (Race_count.get("Asian/ Pacific Islander") == None) else Race_count[
    "Asian/ Pacific Islander"]
Race_count_black = 0 if (Race_count.get("Black/ African American") == None) else Race_count[
    "Black/ African American"]
Race_count_Hispanic = 0 if (Race_count.get("Hispanic/ Latino") == None) else Race_count["Hispanic/ Latino"]
Race_count_native = 0 if (Race_count.get("Native American/ American Indian") == None) else Race_count[
    "Native American/ American Indian"]
Race_count_white = 0 if (Race_count.get("White") == None) else Race_count["White"]
Race_count_prefer_no = 0 if (Race_count.get("Prefer not to answer") == None) else Race_count["Prefer not to answer"]

Race_names = ['Asian/ Pacific Islander', 'Black/ African American', 'Hispanic/ Latino',
              'Native American/ American Indian', 'White', 'Prefer not to answer']
Race_values = [Race_count_asian_pacific, Race_count_black, Race_count_Hispanic, Race_count_native, Race_count_white,
               Race_count_prefer_no]



Dominant_Hand_count = Dominant_Hand.value_counts()
Dominant_Hand_count_left = 0 if (Dominant_Hand_count.get("Right-handed") == None) else Dominant_Hand_count[
    "Right-handed"]
Dominant_Hand_count_right = 0 if (Dominant_Hand_count.get("Left handed") == None) else Dominant_Hand_count[
    "Left handed"]
Dominant_Hand_count_ambi = 0 if (Dominant_Hand_count.get("Ambidextrous") == None) else Dominant_Hand_count[
    "Ambidextrous"]
Dominant_Hand_count_cross = 0 if (Dominant_Hand_count.get("Cross-dominant (Mixed handed)") == None) else \
    Dominant_Hand_count["Cross-dominant (Mixed handed)"]
Dominant_Hand_count_prefer_no = 0 if (Dominant_Hand_count.get("Prefer not to answer") == None) else \
    Dominant_Hand_count["Prefer not to answer"]

Dominant_Hand_count_na = 0 if (Dominant_Hand_count.get("N/A") == None) else Dominant_Hand_count[
    "N/A"]

Dominant_Hand_names = ['Right-handed', 'Left handed', 'Ambidextrous', 'Cross-dominant (Mixed handed)',
                       'Prefer not to answer', 'N/A']
Dominant_Hand_values = [Dominant_Hand_count_left, Dominant_Hand_count_right, Dominant_Hand_count_ambi,
                        Dominant_Hand_count_cross, Dominant_Hand_count_prefer_no, Dominant_Hand_count_na]



Watch_sports_regularly_count = Watch_sports_regularly.value_counts()
Watch_sports_regularly_count_yes = 0 if (Watch_sports_regularly_count.get("Yes") == None) else \
    Watch_sports_regularly_count["Yes"]
Watch_sports_regularly_count_no = 0 if (Watch_sports_regularly_count.get("No") == None) else \
    Watch_sports_regularly_count["No"]
Watch_sports_regularly_count_prefer_no = 0 if (
        Watch_sports_regularly_count.get("Prefer not to answer") == None) else Watch_sports_regularly_count[
    "Prefer not to answer"]

Watch_sports_regularly_names = ['Yes', 'No', 'Prefer not to answer']
Watch_sports_regularly_values = [Watch_sports_regularly_count_yes, Watch_sports_regularly_count_no,
                                 Watch_sports_regularly_count_prefer_no]



Sports_growup_or_last5year_count = Sports_growup_or_last5year.value_counts()
Sports_growup_or_last5year_count_yes = 0 if (Sports_growup_or_last5year_count.get("Yes") == None) else \
    Sports_growup_or_last5year_count["Yes"]
Sports_growup_or_last5year_count_no = 0 if (Sports_growup_or_last5year_count.get("No") == None) else \
    Sports_growup_or_last5year_count["No"]
Sports_growup_or_last5year_count_prefer_no = 0 if (
        Sports_growup_or_last5year_count.get("Prefer not to answer") == None) else \
    Sports_growup_or_last5year_count["Prefer not to answer"]

Sports_growup_or_last5year_names = ['Yes', 'No', 'Prefer not to answer']
Sports_growup_or_last5year_values = [Sports_growup_or_last5year_count_yes, Sports_growup_or_last5year_count_no,
                                     Sports_growup_or_last5year_count_prefer_no]



Education_count = Education.value_counts()
Education_count_tech = 0 if (
        Education_count.get("Tech/ Engineering/ Computer Science/ Aerospace/ Robotics") == None) else \
    Education_count["Tech/ Engineering/ Computer Science/ Aerospace/ Robotics"]
Education_count_life = 0 if (Education_count.get("Life sciences/ Bio-sciences/ Chemical science") == None) else \
    Education_count["Life sciences/ Bio-sciences/ Chemical science"]
Education_count_commerce = 0 if (Education_count.get("Commerce/ Business/ Adminstration") == None) else \
    Education_count["Commerce/ Business/ Adminstration"]
Education_count_humanities = 0 if (Education_count.get("Humanities/ Arts/ Litrature") == None) else Education_count[
    "Humanities/ Arts/ Litrature"]
Education_count_construction = 0 if (Education_count.get("Construction") == None) else Education_count[
    "Construction"]
Education_count_legal = 0 if (Education_count.get("Legal/ Education/ Psychology/ Customer Service") == None) else \
    Education_count["Legal/ Education/ Psychology/ Customer Service"]

Education_names = ['Tech/ Engineering/ Computer Science/ Aerospace/ Robotics',
                   'Life sciences/ Bio-sciences/ Chemical science', 'Commerce/ Business/ Adminstration',
                   'Humanities/ Arts/ Litrature', 'Construction', 'Legal/ Education/ Psychology/ Customer Service']
Education_values = [Education_count_tech, Education_count_life, Education_count_commerce,
                    Education_count_humanities, Education_count_construction, Education_count_legal]



Job_with_3D_count = Job_with_3D.value_counts()
Job_with_3D_count_yes = 0 if (Job_with_3D_count.get("Yes") == None) else Job_with_3D_count["Yes"]
Job_with_3D_count_no = 0 if (Job_with_3D_count.get("No") == None) else Job_with_3D_count["No"]

Job_with_3D_names = ['Yes', 'No']
Job_with_3D_values = [Job_with_3D_count_yes, Job_with_3D_count_no]



Infront_of_computer_count = Infront_of_computer.value_counts()
Infront_of_computer_count_yes = 0 if (Infront_of_computer_count.get("Yes") == None) else Infront_of_computer_count[
    "Yes"]
Infront_of_computer_count_no = 0 if (Infront_of_computer_count.get("No") == None) else Infront_of_computer_count[
    "No"]

Infront_of_computer_names = ['Yes', 'No']
Infront_of_computer_values = [Infront_of_computer_count_yes, Infront_of_computer_count_no]



written_oral_mediums_count = written_oral_mediums.value_counts()
written_oral_mediums_count_yes = 0 if (written_oral_mediums_count.get("Yes") == None) else \
    written_oral_mediums_count["Yes"]
written_oral_mediums_count_no = 0 if (written_oral_mediums_count.get("No") == None) else written_oral_mediums_count[
    "No"]

written_oral_mediums_names = ['Yes', 'No']
written_oral_mediums_values = [written_oral_mediums_count_yes, written_oral_mediums_count_no]



flown_a_drone_count = flown_a_drone.value_counts()
flown_a_drone_count_yes_more = 0 if (flown_a_drone_count.get("Yes, more than 10 times") == None) else \
    flown_a_drone_count["Yes, more than 10 times"]
flown_a_drone_count_yes_less = 0 if (flown_a_drone_count.get("Yes, less than 10 times") == None) else \
    flown_a_drone_count["Yes, less than 10 times"]
flown_a_drone_count_no = 0 if (flown_a_drone_count.get("No, never") == None) else flown_a_drone_count["No, never"]
flown_a_drone_count_prefer_no = 0 if (flown_a_drone_count.get("Prefer not to answer") == None) else \
    flown_a_drone_count["Prefer not to answer"]

flown_a_drone_names = ['Yes, more than 10 times', 'Yes, less than 10 times', 'No, never', 'Prefer not to answer']
flown_a_drone_values = [flown_a_drone_count_yes_more, flown_a_drone_count_yes_less, flown_a_drone_count_no,
                        flown_a_drone_count_prefer_no]



control_robot_count = control_robot.value_counts()
control_robot_count_yes_more = 0 if (control_robot_count.get("Yes, more than 10 times") == None) else \
    control_robot_count["Yes, more than 10 times"]
control_robot_count_yes_less = 0 if (control_robot_count.get("Yes, less than 10 times") == None) else \
    control_robot_count["Yes, less than 10 times"]
control_robot_count_no = 0 if (control_robot_count.get("No, never") == None) else control_robot_count["No, never"]
control_robot_count_prefer_no = 0 if (control_robot_count.get("Prefer not to answer") == None) else \
    control_robot_count["Prefer not to answer"]

control_robot_names = ['Yes, more than 10 times', 'Yes, less than 10 times', 'No, never', 'Prefer not to answer']
control_robot_values = [control_robot_count_yes_more, control_robot_count_yes_less, control_robot_count_no,
                        control_robot_count_prefer_no]



often_playgame_count = often_playgame.value_counts()
often_playgame_count_Daily = 0 if (often_playgame_count.get("Daily") == None) else often_playgame_count["Daily"]
often_playgame_count_couple_week = 0 if (often_playgame_count.get("A couple of times a week") == None) else \
    often_playgame_count["A couple of times a week"]
often_playgame_count_couple_month = 0 if (often_playgame_count.get("A couple of times a month") == None) else \
    often_playgame_count["A couple of times a month"]
often_playgame_count_Rarely = 0 if (often_playgame_count.get("Rarely") == None) else often_playgame_count["Rarely"]
often_playgame_count_Never = 0 if (often_playgame_count.get("Never") == None) else often_playgame_count["Never"]
often_playgame_count_prefer_no = 0 if (often_playgame_count.get("Prefer not to answer") == None) else \
    often_playgame_count["Prefer not to answer"]

often_playgame_names = ['Daily', 'A couple of times a week', 'A couple of times a month', 'Rarely', 'Never',
                        'Prefer not to answer']
often_playgame_values = [often_playgame_count_Daily, often_playgame_count_couple_week,
                         often_playgame_count_couple_month, often_playgame_count_Rarely, often_playgame_count_Never,
                         often_playgame_count_prefer_no]



game_controller_count = game_controller.value_counts()
game_controller_count_Keyboard = 0 if (game_controller_count.get("Keyboard and mouse") == None) else \
    game_controller_count["Keyboard and mouse"]
game_controller_count_Joystick = 0 if (game_controller_count.get("Joystick") == None) else game_controller_count[
    "Joystick"]
game_controller_count_Motion = 0 if (game_controller_count.get(
    "Motion Sensor (Wii Remove, Microsoft Kinect, PlayStation Move, etc)") == None) else game_controller_count[
    "Motion Sensor (Wii Remove, Microsoft Kinect, PlayStation Move, etc)"]
game_controller_count_Gamepad = 0 if (
        game_controller_count.get("Gamepad (Xbox, PlayStation controller.") == None) else game_controller_count[
    "Gamepad (Xbox, PlayStation controller."]
game_controller_count_Steering_wheel = 0 if (game_controller_count.get("Steering wheel") == None) else \
    game_controller_count["Steering wheel"]
game_controller_count_prefer_no = 0 if (game_controller_count.get("Prefer not to answer") == None) else \
    game_controller_count["Prefer not to answer"]

game_controller_names = ['Keyboard and mouse', 'Joystick',
                         'Motion Sensor (Wii Remove, Microsoft Kinect, PlayStation Move, etc)',
                         'Gamepad (Xbox, PlayStation controller.', 'Steering wheel', 'Prefer not to answer']
game_controller_values = [game_controller_count_Keyboard, game_controller_count_Joystick,
                          game_controller_count_Motion, game_controller_count_Gamepad,
                          game_controller_count_Steering_wheel, game_controller_count_prefer_no]



type_of_game_count = type_of_game.value_counts()
type_of_game_count_simulate = 0 if (type_of_game_count.get("Simulations/ Flight Simulators") == None) else \
    type_of_game_count["Simulations/ Flight Simulators"]
type_of_game_count_Adventure = 0 if (type_of_game_count.get("Adventure") == None) else type_of_game_count[
    "Adventure"]
type_of_game_count_RTS = 0 if (type_of_game_count.get("Real-Time Strategy (RTS)") == None) else type_of_game_count[
    "Real-Time Strategy (RTS)"]
type_of_game_count_Puzzle = 0 if (type_of_game_count.get("Puzzle") == None) else type_of_game_count["Puzzle"]
type_of_game_count_Action = 0 if (type_of_game_count.get("Action") == None) else type_of_game_count["Action"]
type_of_game_count_Stealth_Shooter = 0 if (type_of_game_count.get("Stealth Shooter") == None) else \
    type_of_game_count["Stealth Shooter"]
type_of_game_count_FPS = 0 if (type_of_game_count.get("First Person Shooter (FPS)") == None) else \
    type_of_game_count["First Person Shooter (FPS)"]
type_of_game_count_Sports = 0 if (type_of_game_count.get("Sports") == None) else type_of_game_count["Sports"]
type_of_game_count_RPG = 0 if (type_of_game_count.get("Role Playing Game (RPG)") == None) else type_of_game_count[
    "Role Playing Game (RPG)"]
type_of_game_count_Educational = 0 if (type_of_game_count.get("Educational") == None) else type_of_game_count[
    "Educational"]
type_of_game_count_prefer_no = 0 if (type_of_game_count.get("Prefer not to answer") == None) else \
    type_of_game_count["Prefer not to answer"]

type_of_game_count_na = 0 if (type_of_game_count.get("N/A") == None) else \
    type_of_game_count["N/A"]

type_of_game_names = ['Simulations/ Flight Simulators', 'Adventure', 'Real-Time Strategy (RTS)', 'Puzzle', 'Action',
                      'Stealth Shooter', 'First Person Shooter (FPS)', 'Sports', 'Role Playing Game (RPG)',
                      'Educational', 'Prefer not to answer', 'N/A']
type_of_game_values = [type_of_game_count_simulate, type_of_game_count_Adventure, type_of_game_count_RTS,
                       type_of_game_count_Puzzle, type_of_game_count_Action, type_of_game_count_Stealth_Shooter,
                       type_of_game_count_FPS, type_of_game_count_Sports, type_of_game_count_RPG,
                       type_of_game_count_Educational, type_of_game_count_prefer_no, type_of_game_count_na]


