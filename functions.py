from tkinter import messagebox

#here we will fetch the details and verify them
def get_details(CODE,widget_var_list):

    print(f"In get details")
    #print()
    global local_data_list
    local_data_list = [CODE]
    #local_data_list.append(CODE)
    for j in range(9):
        print(f'The value of {j} is')
        print(f'{widget_var_list[j].get()}')
        if j == 6:
            if len(widget_var_list[j].get()) != 10:
                messagebox.showerror(message="Please enter a valid 10 digit mobile number")
                #print(widget_var_list[j].get())
            else:
                local_data_list.append(widget_var_list[j].get())
        else:
            local_data_list.append(widget_var_list[j].get())

    local_data_list.append(" ")

    verify_message = f"The Entered details are: {local_data_list}"
    response = messagebox.askokcancel(message=verify_message)

    if response:
        print(local_data_list)


def update_sheet(code_entry, CODE):
    global local_data_list
    wb = load_workbook(PATH)
    page = wb["Master Sheet"]
    #print("making a new entry")
    #print(local_data_list)
    page.append(local_data_list)
    page['L2'].value = int(CODE)
    wb.save(filename=PATH)

    messagebox.showinfo(message="The entry has been made. "
                                "Now, Please select the Therapies by clicking"
                                " on the Therapy Button")
    #clear_widget(code_entry)


def get_therapy(new_window, code_entry):
    create_therapy_list(new_window, local_data_list)


def clear_widget(code_entry):
    code_entry.delete(0, END)
    for i in range(9):
        if i in [0, 1, 3, 4, 6, 7, 8]:
            widget_list_[i].delete(0, END)
        else:
            widget_var_list[i].set(" ")
