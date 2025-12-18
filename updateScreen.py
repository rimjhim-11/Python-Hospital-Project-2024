from tkinter import *
from data import *
from therapy import create_therapy_list
from patient_window import CreateWidget
from tkinter import messagebox

def get_update_screen(root_window: object, local_data_list: object) -> object:
    update_screen = Toplevel(root_window)
    update_screen.title("Update Entry")

    # specify size
    update_screen.geometry("800x600")
    update_screen.config(padx=10, pady=10, bg='Khaki')
    update_screen.grid_columnconfigure(2, weight=1)
    update_screen.wm_transient(root_window)

    code = local_data_list[0]
    code_label = Label(update_screen, text=f'CODE: {code}',
                       bg='Khaki', font=('Courier', 12, 'bold'))
    code_label.grid(row=0, column=1)
    # for i in range(9):
    update_ = CreateWidget(update_screen)
    for i in range(9):
        print(f"widget details {update_.widget_var_list[i].get()}")
        print(f'The local_data_list[i+1] is {local_data_list[i+1]} and i is  {i}')
        update_.widget_var_list[i].set(local_data_list[i+1])
    update_entry_button = Button(update_screen, text="Update Entry",
                                 command=lambda: update_with_new_data(code, update_, local_data_list))
    update_entry_button.config(width=20, height=1)
    update_entry_button.grid(row=10, column=3)
    therapy_button = Button(update_screen, text='Select Therapies',
                            command=lambda: get_therapy(update_screen, "", local_data_list))

    #replaced code_entry with ""
    therapy_button.config(width=20, height=1)

    therapy_button.grid(row=11, column=3)

    exit_button = Button(update_screen, text='Exit',
                         command=lambda: update_screen.destroy())
    exit_button.config(width=20, height=2)
    exit_button.grid(row=12, column=3)


def get_therapy(new_window, code_entry, local_data_list):
    create_therapy_list(new_window, local_data_list)


def update_with_new_data(code, update_, local_data_list):
    wb = load_workbook(PATH)
    page = wb["Master Sheet"]
    code_temp = int(code)
    entry_found = False
    for row in range(page.max_row+1):
        row += 1
        cell = page.cell(row, 1)
        print(f'Cell.value = {cell.value} and code_temp = {code_temp}')
        if cell.value == code_temp:
            print('Found entry in update screen')
            entry_found = True
            for i in range(9):
                temp_data = update_.widget_var_list[i].get()
                local_data_list[i+1] = temp_data
                cell_ = page.cell(row, i+2)
                cell_.value = temp_data
                #cell_.value = temp_data

        if entry_found:
            break

    print("Saving data")
    messagebox.showinfo(title='Update status', message='The record has been updated')
    wb.save(filename=PATH)
