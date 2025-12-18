from patient_window import *
import pandas as pd
from fetch import *
from transaction import *
from updateScreen import *

def config_window():
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Hospital Data")
    root.config(pady=30, padx=20, bg='Khaki')
    for i in range(4):
        root.grid_rowconfigure(i, weight=1)

    for j in range(2):
        root.grid_columnconfigure(j, weight=1)


def main_window():
    global IMAGE_1, IMAGE_2

    canvas = Canvas(root, bg="Khaki", width=1000, height=200,highlightthickness=0)
    img = PhotoImage(file=IMAGE_1)
    img2 = PhotoImage(file=IMAGE_2)

    label = Label(image=img)
    label.image = img

    label2 = Label(image=img2)
    label2.image = img2
    # The Label widget is a standard (Tkinter widget used to display a text or image on the
    # screen.
    canvas.create_image(600, 100, image=label.image)
    print("header image")
    canvas.grid(row=0, column=0, sticky=N+S+E+W)

    canvas2 = Canvas(root, bg="Khaki", width=1000, height=200, highlightthickness=0)
    canvas2.create_image(600, 100, image=label2.image)
    print("trailer image")
    canvas2.grid(row=5, column=0, sticky=N+S+E+W)

    new_button = Button(text='New Patient', command=new_func, width=20, height=2,
                        bg='DarkOrange', font=('MS Sans Serif', 12, 'bold'))
    new_button.grid(row=1, column=0)

    old_button = Button(text='Old Patient', command=old_func, width=20, height=2,
                        bg='DarkOrange', font=('MS Sans Serif', 12, 'bold'))
    old_button.grid(row=2, column=0)

    calc_button = Button(text='Get Transactional Details', command=get_transaction_details, width=20, height=2,
                         bg='DarkOrange', font=('MS Sans Serif', 12, 'bold'))
    calc_button.grid(row=3, column=0)

    exit_button = Button(text='Exit', command=exit_root, width=20, height=2,
                        bg='DarkOrange', font=('MS Sans Serif', 12, 'bold'))
    exit_button.grid(row=4, column=0)


def new_func():
    global CODE
    new_window = Toplevel(root)
    new_window.title("New Patient Entry")

    # specify size
    new_window.geometry("800x600")
    new_window.config(padx=10, pady=10, bg='Khaki')
    new_window.grid_columnconfigure(2, weight=1)
    new_window.wm_transient(root)

    code_label = Label(new_window, text='Code:', bg='Khaki', font=('Courier', 12, 'bold'))
    code_label.grid(row=0, column=0)

    code_var = tkinter.StringVar()
    code_entry = Entry(new_window, textvariable=code_var, font=('Courier', 12, 'bold'), width=50)
    code_entry.grid(row=0, column=1)

    generate_code_button = Button(new_window, text='Generate Code',
                                  command=lambda: generate_code(code_var))

    generate_code_button.grid(row=0, column=3)
    code_var.set(CODE)

    # creating other labels
    # for i in range(9):
    create_ = CreateWidget(new_window)

    text = "Create Entry"
    create_entry_buttons(new_window, get_details,
                         update_sheet, clear_widget,
                         get_therapy, code_entry, text, create_)


def generate_code(code_var):
    global CODE
    code_var = code_var
    df = pd.read_excel(PATH)
    CODE = int((df['Last Generated Code'].values[0] + 1))
    code_var.set(CODE)


def get_details(create_):

    print(f"In get details")
    global local_data_list
    local_data_list = [CODE]


    for j in range(9):
        all_good = True
        print(f'The value of {j} is')
        print(f'{create_.widget_var_list[j].get()}')
        if j == 6 and len(create_.widget_var_list[j].get()) != 10:
            #if len(create_.widget_var_list[j].get()) != 10:
            messagebox.showerror(message="Please enter a valid 10 digit mobile number")
            print("Please enter a valid 10 digit mobile number")
            print(create_.widget_var_list[j].get())
            all_good = False
        elif j == 1 and (int(create_.widget_var_list[j].get()) not in range(1, 120)):
            print(f"Age entered is: {create_.widget_var_list[j].get()}")
            #if int(create_.widget_var_list[j].get()) not in range(1, 120):
            messagebox.showerror(message="Please enter a valid age between 0 and 120")
            print("Please enter a valid age")
            print(create_.widget_var_list[j].get())
            all_good = False
        elif j == 4 and create_.widget_var_list[j].get() == "":
            #if create_.widget_var_list[j].get() == "":
            messagebox.showerror(message="Please enter a district. This field cannot be empty")
            print("Please enter a valid age")
            print(create_.widget_var_list[j].get())
            all_good = False

        elif j == 8 and create_.widget_var_list[j].get() == '':
            #if int(create_.widget_var_list[j].get()) not in range(0, 1000000):
            messagebox.showerror(message="Please enter a numeric value for deposit. Enter 0 if no Deposit")
            print("Please enter a valid deposit amount")
            print(create_.widget_var_list[j].get())
            all_good = False
        else:
            local_data_list.append(create_.widget_var_list[j].get())
            #messagebox.showinfo(title='Information', message="Verified all details. Please proceed")
            #all_good = True

    local_data_list.append(" ")
    if all_good:
        verify_message = f"The Entered details are: {local_data_list}"
        messagebox.showinfo(title='Information', message="Verified all details. Please proceed")
        response = messagebox.askokcancel(message=verify_message)

    if response:
        print(local_data_list)


def update_sheet(code_entry):
    global local_data_list
    wb = load_workbook(PATH)
    page = wb["Master Sheet"]
    page.append(local_data_list)
    page['L2'].value = int(CODE)
    wb.save(filename=PATH)

    messagebox.showinfo(message="The entry has been made. "
                                "Now, Please select the Therapies by clicking"
                                " on the Therapy Button")


def get_therapy(new_window, code_entry):
    create_therapy_list(new_window, local_data_list)


def clear_widget(code_entry, create_):
    code_entry.delete(0, END)
    for i in range(9):
        if i in [0, 1, 3, 4, 6, 7, 8]:
            create_.widget_list_[i].delete(0, END)
        else:
            create_.widget_var_list[i].set(" ")


def old_func():
    old_window = Toplevel(root)
    old_window.title("Get Old Patient details")

    # specify size
    old_window.geometry("800x150")
    old_window.config(padx=10, pady=10, bg='Khaki')
    old_window.grid_columnconfigure(2, weight=1)

    # wm_transient(root) ensures the child window is always in front of the root window
    old_window.wm_transient(root)

    code_label = Label(old_window, text='Code:', bg='Khaki', font=('Courier', 12, 'bold'))
    code_label.grid(row=0, column=0)

    code_var = tkinter.StringVar()
    code_entry = Entry(old_window, textvariable=code_var, font=('Courier', 12, 'bold'), width=50)
    code_entry.grid(row=0, column=1)

    get_by_code_button = Button(old_window, text='Get details by Code',
                                command=lambda: old_window.after(1000,
                                                                 fetch_from_sheet(code_var, 1, old_window, local_data_list)))

    get_by_code_button.grid(row=0, column=3)

###################################################################
    mobile_label = Label(old_window, text='Mobile:', bg='Khaki', font=('Courier', 12, 'bold'))
    mobile_label.grid(row=1, column=0)

    mobile_var = tkinter.StringVar()
    mobile_entry = Entry(old_window, textvariable=mobile_var, font=('Courier', 12, 'bold'), width=50)
    mobile_entry.grid(row=1, column=1)

    get_by_mobile_button = Button(old_window, text='Get details by Mobile Number',
                                command=lambda: fetch_from_sheet(mobile_var, 8, old_window, local_data_list))

    get_by_mobile_button.grid(row=1, column=3)

    district_label = Label(old_window, text='District:', bg='Khaki', font=('Courier', 12, 'bold'))
    district_label.grid(row=2, column=0)

    district_var = tkinter.StringVar()
    district_entry = Entry(old_window, textvariable=district_var, font=('Courier', 12, 'bold'), width=50)
    district_entry.grid(row=2, column=1)

    get_by_district_button = Button(old_window, text='Get details by District',
                                  command=lambda: fetch_from_sheet(district_var, 6, old_window, local_data_list))

    get_by_district_button.grid(row=2, column=3)

    exit_screen_button = Button(old_window, text='Exit',
                                    command=lambda: old_window.destroy())

    exit_screen_button.grid(row=3, column=1)


def get_transaction_details():
    trans_screen = Toplevel(root)
    trans_screen.title("Transactional Window")

    # specify size
    trans_screen.geometry("400x100")
    trans_screen.config(padx=10, pady=10, bg='medium spring green')
    trans_screen.grid_columnconfigure(2, weight=1)
    trans_screen.wm_transient(root)

    daily_trans_button = Button(trans_screen, text="Close Daily Transaction",
                                  command=daily_transaction_sheet_update)

    daily_trans_button.grid(row=0, column=0)

    add_trans_button = Button(trans_screen, text="Get Transaction Summary Datewise",
                              command=lambda:get_datewise_collection(trans_screen))

    add_trans_button.grid(row=1, column=0)

    exit_trans_button = Button(trans_screen,
                               text="Exit Screen",
                               command=lambda: trans_screen.destroy())

    exit_trans_button.grid(row=2, column=0)

    #pass

def exit_root():
    root.destroy()


if __name__ == '__main__':
    root = Tk()
    config_window()
    main_window()
    #print(age)
    root.mainloop()