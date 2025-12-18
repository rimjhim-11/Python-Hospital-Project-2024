from tkinter import *
from tkinter import messagebox
from data import *


def calculate(therapy_window, local_data_list, var):
    total_fees = 0
    therapies = []
    therapy_names = ""
    print(total_fees)
    therapies.append(local_data_list[0])
    therapies.append(local_data_list[1])
    idx = 0
    for var_value in var:
        therapies.append(var_value.get())
        #therapies.append()
        total_fees += var_value.get()
        if var_value.get() > 0:
            print(f'One of the therapy selected is :{therapy_name[idx]}')
            therapy_names =therapy_names  + therapy_name[idx] + ','
        idx += 1
    print("Therapies selected are:")
    print(therapy_names)
    print(f'Deposit is {local_data_list[9]}')
    print(f'total_fees: {total_fees}')
    if local_data_list[9] == None:
        local_data_list[9] = 0
    if total_fees < int(local_data_list[9]):
        local_data_list[9] = int(local_data_list[9]) - total_fees
        print(f'Updated deposit is: {local_data_list[9]}')
        total_fees = 0
    else:
        total_fees = abs(total_fees - int(local_data_list[9]))
        local_data_list[9] = int(local_data_list[9]) - total_fees
        if local_data_list[9] < 0:
            local_data_list[9] = 0
    response = messagebox.askokcancel(title="Total Fees",
                                      message=f'The total amount to be collected is {total_fees}.'
                                              f'Remaining deposit is {local_data_list[9]}'
                                              f' Press Ok to proceed and update the same in the '
                                              f'Update section')

    if response:
        update_daily_transaction(therapies, therapy_names)
        therapy_window.destroy()


def create_therapy_list(new_window, local_data_list):
    var = []
    therapy_window = Toplevel(new_window)
    therapy_window.title("Therapies")

    # specify size
    therapy_window.geometry("800x600")
    therapy_window.config(padx=10, pady=10, bg='Khaki')
    therapy_window.grid_columnconfigure(2, weight=1)
    col_value = 10
    row_value = 0
    for key, value in therapy_list_price.items():
        var_ = IntVar()
        row_value += 1
        check_box = Checkbutton(therapy_window, text=therapy_name[key-1]
                                , variable=var_, onvalue=value,
                                offvalue=0, font=('courier', 12, 'bold'))
        check_box.config(bg='Khaki', highlightthickness=0)
        check_box.grid(row=row_value, column=col_value, sticky='w')
        if row_value == 15:
            row_value = 0
            col_value += 50

        var.append(var_)
        #therapies.append(check_box.cget("text"))
    button = Button(therapy_window, text='Confirm', command=lambda:calculate(therapy_window, local_data_list, var))
    button.grid(row=20, column=20, sticky='w', pady=50, padx=50)
    
    
def update_daily_transaction(therapies, therapy_names):
    wb = load_workbook(PATH)
    page2 = wb["Daily Transactions"]
    print("making a new entry in daily transaction sheet")
    print(therapies)
    page2.append(therapies)
    wb.save(filename=PATH)
    messagebox.showinfo(message="The Therapies have been added to the Daily Transactions Sheet")
    messagebox.showinfo(message="Closing the Therapy Selection Screen")
    update_therapy_history(therapies[0], therapies[1], therapy_names)
    update_transaction_history(therapies)

#update the therapy_history sheet
def update_therapy_history(code_t, name_t, therapy_names):

    temp_data_t = []
    temp_data_t.append(code_t)
    temp_data_t.append(name_t)
    therapy_entry_found = False
    temp_data_t.append(therapy_names)
    temp_data_t.append(today_date)
    wb = load_workbook(PATH)
    page3 = wb["Therapy History"]
    for row in range(page3.max_row + 1):
        row += 1
        cell = page3.cell(row, 1)
        print(f'Cell is: {cell.value}  and code_t is:{code_t}')
        if str(code_t) == str(cell.value):
            print("Found a match in the therapy history")
            temp_therapy_history = page3.cell(row, 3).value
            therapy_names += f', {temp_therapy_history} , '
            page3.cell(row, 3).value = therapy_names
            page3.cell(row, 4).value = today_date
            print(f"THERAPY NAMES AFTER UPDATION: {therapy_names}")
            therapy_entry_found = True
        if therapy_entry_found:
            break
    else:
        page3.append(temp_data_t)

    #temp_data_t.append(therapy_names)
    wb.save(filename=PATH)
    print("Data has been added/ appended")


def update_transaction_history(therapies_):
    therapy_history = [today_date]
    entry_data = therapy_history + therapies_
    wb = load_workbook(PATH)
    page2 = wb["Transaction History"]
    print("making a new entry in daily transaction sheet")
    page2.append(entry_data)
    wb.save(filename=PATH)

