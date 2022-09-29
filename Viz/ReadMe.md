
Operation:

• Open the programme by typing python3 GUI.py
• Select two variables from the left list box
• Enter total participants number on the top-right corner
• Button on the right:
	◦ Show all single graphs
		‣ Display a combined graph with all the variables distribution
	◦ Show selected variable
		‣ Display a prompt that shows which variables have been selected
	◦ Compare 2 variables without predict
		‣ Display a graph that compares two selected variables
	◦ Compare 2 variables with predict
		‣ Display a graph that compares two selected variables and with prediction
	◦ Show participants number
		‣ Display a prompt that shows how many participants entered





Code:

• visualization.py
	◦ Function:
		‣ simple_distribution()
			• Display each variable distribution and combine all together into one graph
		‣ computer_two_variables()
			• Create a dataframe for two input arguments.
			• Plot this dataframe and display two compared variables
		‣ computer_two_variables_with_predict()
			• Create a dataframe for two input arguments.
			• Create a dataframe with prediction value.
			• Plot both dataframes
• GUI.py
	◦ Function:
		‣ show_select()
			• Prompt which variables selected
		‣ computer_two()
			• Call computer_two_variables() from visualization.py
		‣ computer_two_with_predict()
			• Call computer_two_variables_with_predict() from visualization.py
		‣ show_all()
			• Call simple_distribution() from visualization.py
		‣ show_participants()
			• Prompt how many participants entered
		‣ main()
			• Set the list box, text entry and all buttons







