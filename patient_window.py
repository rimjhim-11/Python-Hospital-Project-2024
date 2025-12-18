import tkinter
from tkinter import *
from data import *
from data import gender, states
#import data


def create_entry_buttons(window, func1, func2, func3, func4, code_entry, text1, create_s):
    verify_entry_button = Button(window, text='Verify Entry',
                                 command=lambda: func1(create_s))

    verify_entry_button.config(width=20, height=1)
    verify_entry_button.grid(row=11, column=3)

    # create the create entry button
    create_entry_button = Button(window, text=text1,
                                 command=lambda: func2(code_entry))
    create_entry_button.config(width=20, height=1)
    create_entry_button.grid(row=12, column=3)

    clear_button = Button(window, text='Clear Screen',
                          command=lambda: func3(code_entry, create_s))
    clear_button.config(width=20, height=1)

    clear_button.grid(row=14, column=3)

    therapy_button = Button(window, text='Select Therapies',
                            command=lambda: func4(window, code_entry))
    therapy_button.config(width=20, height=1)

    therapy_button.grid(row=15, column=3)

    exit_button = Button(window, text='Exit',
                         command=lambda: window.destroy())
    exit_button.config(width=20, height=2)

    exit_button.grid(row=16, column=1)


class CreateWidget:
    def __init__(self, window):
        #widget_list
        widget_list = ['Name', 'Age', 'Gender', 'Address', 'District',
                       'State', 'Mobile Number', 'Email', 'Deposit']
        self.widget_var_list = []

        self.widget_list_ = []

        for i in range(9):

            self.label = Label(window, text=widget_list[i], bg='Khaki', font=('Courier', 12, 'bold'))
            self.label.grid(row=i + 1, column=0)
            if i in [0, 1, 3, 4, 6, 7, 8]:
                if i in [1]:
                    self.var = tkinter.IntVar()
                    #self.var.set(0)
                else:
                    self.var = tkinter.StringVar()

                self.entry = Entry(window,
                               textvariable=self.var, font=('Courier', 12, 'bold'), width=50)
                self.entry.grid(row=i+1, column=1)
                self.widget_list_.append(self.entry)
            elif i == 2:
                self.var = tkinter.StringVar()
                self.var.set(' ')
                self.gender_drop = OptionMenu(window, self.var, *gender)
                self.gender_drop.grid(row=i + 1, column=1)
                self.widget_list_.append(self.gender_drop)
            elif i == 5:
                self.var = tkinter.StringVar()
                self.var.set(' ')
                self.states_drop = OptionMenu(window, self.var, *states)
                self.states_drop.grid(row=i + 1, column=1)
                self.widget_list_.append(self.states_drop)

            self.widget_var_list.append(self.var)
