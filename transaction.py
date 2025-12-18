import tkinter

from data import *
from tkinter import messagebox
from tkinter import *
from matplotlib import pyplot as plt


def daily_transaction_sheet_update():
    workbook = load_workbook(PATH)
    collections = []
    page = workbook["Daily Transactions"]
    max_rows = page.max_row + 1
    max_cols = page.max_column + 1

    print(f"max_cols: {max_cols} and max_rows: {max_rows}")
    collections.append(today_date)
    for col in range(3, max_cols):
        sum_collection = 0
        for row in range(2, max_rows):
            sum_collection += page.cell(row, col).value
        collections.append(sum_collection)

    messagebox.showinfo(title="Today's Total Collection", message=f'{today_date}: {collections}')
    print(f'Total Collections {collections}')
    update_datewise_collection_sheet(collections)


def update_datewise_collection_sheet(collection_):
    #temp_trans_data = []
    #temp_trans_data.append(today_date)
    workbook = load_workbook(PATH)
    page = workbook["Datewise per Therapy collection"]
    page.append(collection_)
    workbook.save(PATH)

    #clear data from the daily transaction sheet:
    page_daily = workbook['Daily Transactions']
    max_rows = page_daily.max_row
    max_cols = page_daily.max_column

    for row in range(2, max_rows+1):
        for cols in range(1, max_cols+1):
            cell = page_daily.cell(row, cols)
            cell.value = 0
    workbook.save(PATH)

def get_datewise_collection(screen):
    date_popup = Toplevel(screen)
    date_popup.geometry("200x60")
    date_popup.config(padx=10, pady=10, bg='dark khaki')
    date_popup.wm_transient(screen)
    date_var = tkinter.StringVar()
    date_var.set('dd-mm-yyyy')
    date = Entry(date_popup, textvariable=date_var, font=('calibre', 10, 'normal'))
    date.grid(row=0, column=0)

    ok_button = Button(date_popup,text='Ok',
                                  command=lambda: get_date(date_var))
    ok_button.grid(row=1, column=0)
    #date.pack()


def get_date(date_):
    date_str = date_.get()
    fetch_summary_from_sheet(date_str)


def fetch_summary_from_sheet(date_summary):
    workbook = load_workbook(PATH)
    page = workbook["Datewise per Therapy collection"]
    max_row = page.max_row
    max_col = page.max_column

    display_data = []
    x_axis = []
    y_axis = []

    found_date = False
    for row in range(2, max_row+1):
        cell = page.cell(row, 1)
        if str(date_summary) in str(cell.value):
            found_date = True
            print("found matching date data")
            for col in range(2, max_col):
                if page.cell(row, col).value > 0:
                    temp_data = f'{therapy_name[col-2]}: Rs.{page.cell(row, col).value}'
                    x_axis.append(therapy_name[col-2][:7])
                    y_axis.append(page.cell(row, col).value)
                    display_data.append(temp_data)
        if found_date:
            #messagebox.showinfo(title='Collections',
            #                    message=f'Collections for the date {date_summary} is {display_data}')
            bars = plt.bar(x_axis, y_axis, width=0.4)

            plt.show()
            break
    else:
        messagebox.showinfo(title='No Data', message=f"No entry found for this date: {date_summary}")









    #pass




