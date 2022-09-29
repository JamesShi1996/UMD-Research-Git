'''
 questions:
    major:
        1. add predict value and show


    minor:
        1: change front style in compare two variable graph (incline)
        2: change show all graph front problem


'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')

import recom_gender
import visualization


def show_select():
    temp_list = list()

    selected = listbox.curselection()

    for i in selected:
        val = listbox.get(i)
        temp_list.append(val)
    string = "Here is your choice: \n"
    another_line = '\n'
    str123 = another_line.join(temp_list)
    string = string + str123
    messagebox.showinfo("Selected", "%s" % string)


def computer_two():
    temp_list = list()
    selected = listbox.curselection()
    for i in selected:
        val = listbox.get(i)
        temp_list.append(val)

    visualization.computer_two_variables(temp_list[0],temp_list[1])


def computer_two_with_predict():
    temp_list = list()
    selected = listbox.curselection()
    for i in selected:
        val = listbox.get(i)
        temp_list.append(val)

    visualization.computer_two_variables_with_predict(temp_list[0], temp_list[1])


def show_all():
    visualization.simple_distribution()


def main():
    global top
    top = Tk()

    frame1 = Frame(top)
    frame1.pack(side=LEFT, padx=10, pady=10)
    global listbox
    listbox = Listbox(frame1, selectmode='multiple')
    listbox.pack(padx=10, pady=10)
    listbox.IntegralHeight = FALSE
    listbox.Height = 100

    list_all = visualization.df.iloc[:, 2::]

    for item in list_all:
        listbox.insert(END, item)

    frame2 = ttk.Frame(top)
    frame2.pack(side=RIGHT, pady=10)

    ttk.Button(frame2, text='Show all single graphs', command=show_all).pack(fill=X)
    ttk.Button(frame2, text='Show selected variable', command=show_select).pack(fill=X)
    ttk.Button(frame2, text='Compare 2 variables without predict', command=computer_two).pack(fill=X)
    ttk.Button(frame2, text='Compare 2 variables with predict', command=computer_two_with_predict).pack(fill=X)

    frame3 = ttk.Frame(top)
    frame3.pack(side=TOP, pady=10)



    top.title("UI of Data Visualization")
    # top.geometry("700x500")

    # app = Window(top)
    top.mainloop()



if __name__ == "__main__": main()


