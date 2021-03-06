from tkinter import *
import pandas as pd
import openpyxl

COMPETITORS_DATABASE_LOCATION = 'C:/School App Project/competitors database.xlsx'
STUDENTS_DATABASE_LOCATION = 'C:/School App Project/students database.xlsx'


def add_competitor():
    global add_competitor_screen
    add_competitor_screen = Toplevel(main_screen)
    add_competitor_screen.title("Add Competitor Page")
    add_competitor_screen.geometry("300x300")

    global first_name_c
    global last_name_c
    global id_c
    global class_name_c
    global first_name_entry_c
    global last_name_entry_c
    global id_entry_c
    global class_name_entry_c
    first_name_c = StringVar()
    last_name_c = StringVar()
    id_c = StringVar()
    class_name_c = StringVar()
    # Set label for user's instruction
    Label(add_competitor_screen, text="Please enter details below", bg="blue", fg="white").pack()
    Label(add_competitor_screen, text="").pack()
    # Set first name label
    first_name_lable = Label(add_competitor_screen, text="First Name * ")
    first_name_lable.pack()
    first_name_entry_c = Entry(add_competitor_screen, textvariable=first_name_c)
    first_name_entry_c.pack()
    # Set last name label
    last_name_lable = Label(add_competitor_screen, text="Last Name * ")
    last_name_lable.pack()
    last_name_entry_c = Entry(add_competitor_screen, textvariable=last_name_c)
    last_name_entry_c.pack()
    # Set id label
    id_lable = Label(add_competitor_screen, text="Id * ")
    id_lable.pack()
    id_entry_c = Entry(add_competitor_screen, textvariable=id_c)
    id_entry_c.pack()
    # Set class name label
    class_name_lable = Label(add_competitor_screen, text="Class Name * ")
    class_name_lable.pack()
    class_name_entry_c = Entry(add_competitor_screen, textvariable=class_name_c)
    class_name_entry_c.pack()
    # Set Add Competitor button
    Label(add_competitor_screen, text="").pack()
    Button(add_competitor_screen, text="Add Competitor", width=15, height=1, bg="blue", fg="white", command=new_competitor_user).pack()


def add_student():
    global add_student_screen
    add_student_screen = Toplevel(main_screen)
    add_student_screen.title("Add Student Page")
    add_student_screen.geometry("300x350")

    global first_name_s
    global last_name_s
    global id_s
    global class_name_s
    global phone_number_s
    global first_name_entry_s
    global last_name_entry_s
    global id_entry_s
    global class_name_entry_s
    global phone_number_entry_s
    first_name_s = StringVar()
    last_name_s = StringVar()
    id_s = StringVar()
    class_name_s = StringVar()
    phone_number_s = StringVar()
    # Set label for user's instruction
    Label(add_student_screen, text="Please enter details below", bg="blue", fg="white").pack()
    Label(add_student_screen, text="").pack()
    # Set first name label
    first_name_lable = Label(add_student_screen, text="First Name * ")
    first_name_lable.pack()
    first_name_entry_s = Entry(add_student_screen, textvariable=first_name_s)
    first_name_entry_s.pack()
    # Set last name label
    last_name_lable = Label(add_student_screen, text="Last Name * ")
    last_name_lable.pack()
    last_name_entry_s = Entry(add_student_screen, textvariable=last_name_s)
    last_name_entry_s.pack()
    # Set id label
    id_lable = Label(add_student_screen, text="Id * ")
    id_lable.pack()
    id_entry_s = Entry(add_student_screen, textvariable=id_s)
    id_entry_s.pack()
    # Set class name label
    class_name_lable = Label(add_student_screen, text="Class Name * ")
    class_name_lable.pack()
    class_name_entry_s = Entry(add_student_screen, textvariable=class_name_s)
    class_name_entry_s.pack()
    # Set phone number label
    class_name_lable = Label(add_student_screen, text="Phone Number * ")
    class_name_lable.pack()
    phone_number_entry_s = Entry(add_student_screen, textvariable=phone_number_s)
    phone_number_entry_s.pack()
    # Set Add Competitor button
    Label(add_student_screen, text="").pack()
    Button(add_student_screen, text="Add Student", width=15, height=1, bg="blue", fg="white", command=new_student_user).pack()


def new_competitor_user():
    first_name_info = str(first_name_c.get())
    last_name_info = str(last_name_c.get())
    id_info = str(id_c.get())
    class_name_info = str(class_name_c.get())
    first_name_entry_c.delete(0, END)
    last_name_entry_c.delete(0, END)
    id_entry_c.delete(0, END)
    class_name_entry_c.delete(0, END)
    wbC = openpyxl.load_workbook(COMPETITORS_DATABASE_LOCATION)
    sheet = wbC.active
    counter = 2
    block_name = "A" + str(counter)
    while sheet[block_name].value is not None:
        counter += 1
        block_name = "A" + str(counter)
    sheet["A" + str(counter)] = first_name_info
    sheet["B" + str(counter)] = last_name_info
    sheet["C" + str(counter)] = 0
    sheet["D" + str(counter)] = class_name_info
    sheet["E" + str(counter)] = int(id_info)
    wbC.save(COMPETITORS_DATABASE_LOCATION)


def new_student_user():
    first_name_info = str(first_name_s.get())
    last_name_info = str(last_name_s.get())
    id_info = str(id_s.get())
    class_name_info = str(class_name_s.get())
    phone_number_info = str(phone_number_s.get())
    first_name_entry_s.delete(0, END)
    last_name_entry_s.delete(0, END)
    id_entry_s.delete(0, END)
    class_name_entry_s.delete(0, END)
    phone_number_entry_s.delete(0, END)
    wbS = openpyxl.load_workbook(STUDENTS_DATABASE_LOCATION)
    sheet = wbS.active
    counter = 2
    block_name = "A" + str(counter)
    while sheet[block_name].value is not None:
        counter += 1
        block_name = "A" + str(counter)
    sheet["A" + str(counter)] = first_name_info
    sheet["B" + str(counter)] = last_name_info
    sheet["C" + str(counter)] = "n"
    sheet["D" + str(counter)] = class_name_info
    sheet["E" + str(counter)] = int(id_info)
    sheet["F" + str(counter)] = int(phone_number_info)
    wbS.save(STUDENTS_DATABASE_LOCATION)


def competitors_table():
    global competitors_table_screen
    competitors_table_screen = Toplevel(main_screen)
    competitors_table_screen.title("Competitors Table Page")
    competitors_table_screen.geometry("740x500")

    # get the competitors values from the excel file
    data_in = pd.read_excel(COMPETITORS_DATABASE_LOCATION)
    df = pd.DataFrame(data_in, columns=['FirstName', 'LastName', 'VotesNumber', 'Class', 'Id', 'Picture'])
    competitors_list = df.values.tolist()
    for i in range(7):
        e = Entry(competitors_table_screen, width=20, fg='blue')
        e.grid(row=0, column=i)
        if i == 0:
            e.insert(END, 'Delete')
        elif i == 1:
            e.insert(END, 'FirstName')
        elif i == 2:
            e.insert(END, 'LastName')
        elif i == 3:
            e.insert(END, 'VotesNumber')
        elif i == 4:
            e.insert(END, 'Class')
        elif i == 5:
            e.insert(END, 'Id')
        elif i == 6:
            e.insert(END, 'Picture')

    global check_boxes_list_c
    check_boxes_list_c = list()
    for i in range(len(competitors_list)):
        var = IntVar()
        check_boxes_list_c.append(var)
        cb = Checkbutton(competitors_table_screen, text="Delete?", variable=check_boxes_list_c[i]).grid(row=i + 1, column=0)
        for j in range(6):
            e = Entry(competitors_table_screen, width=20, fg='blue')
            e.grid(row=i+1, column=j+1)
            e.insert(END, competitors_list[i][j])

    Button(competitors_table_screen, text="Delete Competitors", height="2", width="20", command=delete_competitors).grid(row=len(competitors_list)+2, column=2)


def remove_row(sheet, row):
    sheet.delete_rows(row[0].row, 1)


def delete_competitors():
    check_boxes_list_info = check_boxes_list_c
    wbC = openpyxl.load_workbook(COMPETITORS_DATABASE_LOCATION)
    sheet = wbC.active
    winners_visibility = str(sheet["G2"].value)
    for i in range(len(check_boxes_list_info)):
        if check_boxes_list_info[i].get() == 1:
            remove_row(sheet, sheet[i+2])
            if i == 0:
                sheet["G2"] = winners_visibility
    wbC.save(COMPETITORS_DATABASE_LOCATION)


def students_table():
    global students_table_screen
    students_table_screen = Toplevel(main_screen)
    students_table_screen.title("Students Table Page")
    students_table_screen.geometry("870x500")

    # get the competitors values from the excel file
    data_in = pd.read_excel(STUDENTS_DATABASE_LOCATION)
    df = pd.DataFrame(data_in, columns=['FirstName', 'LastName', 'AlreadyVoted', 'Class', 'Id', 'PhoneNumber'])
    students_list = df.values.tolist()

    for i in range(7):
        e = Entry(students_table_screen, width=20, fg='blue')
        e.grid(row=0, column=i)
        if i == 0:
            e.insert(END, 'Delete')
        elif i == 1:
            e.insert(END, 'FirstName')
        elif i == 2:
            e.insert(END, 'LastName')
        elif i == 3:
            e.insert(END, 'AlreadyVoted')
        elif i == 4:
            e.insert(END, 'Class')
        elif i == 5:
            e.insert(END, 'Id')
        elif i == 6:
            e.insert(END, 'PhoneNumber')

    global check_boxes_list_s
    check_boxes_list_s = list()
    for i in range(len(students_list)):
        var = IntVar()
        check_boxes_list_s.append(var)
        cb = Checkbutton(students_table_screen, text="Delete?", variable=check_boxes_list_s[i]).grid(row=i + 1, column=0)
        for j in range(6):
            e = Entry(students_table_screen, width=20, fg='blue')
            e.grid(row=i + 1, column=j + 1)
            e.insert(END, students_list[i][j])

    Button(students_table_screen, text="Delete Students", height="2", width="20",command=delete_students).grid(row=len(students_list) + 2, column=2)


def delete_students():
    check_boxes_list_info = check_boxes_list_s
    wbC = openpyxl.load_workbook(STUDENTS_DATABASE_LOCATION)
    sheet = wbC.active
    for i in range(len(check_boxes_list_info)):
        if check_boxes_list_info[i].get() == 1:
            remove_row(sheet, sheet[i+2])
    wbC.save(STUDENTS_DATABASE_LOCATION)


def check_winners_visibility():
    data_in = pd.read_excel(COMPETITORS_DATABASE_LOCATION)
    df = pd.DataFrame(data_in, columns=['FirstName', 'LastName', 'VotesNumber', 'Class', 'Id', 'Picture', 'CanSee'])
    competitors_list = df.values.tolist()
    if str(competitors_list[0][6]) == "n":
        return "red"
    else:
        return "green"


def set_winners_visibility():
    global winners_visibility_button_color
    wbC = openpyxl.load_workbook(COMPETITORS_DATABASE_LOCATION)
    sheet = wbC.active
    if str(winners_visibility_button_color) == "red":
        winners_visibility_button.configure(bg="green")
        winners_visibility_button_color = "green"
        sheet["G2"] = "y"
    elif str(winners_visibility_button_color) == "green":
        winners_visibility_button.configure(bg="red")
        winners_visibility_button_color = "red"
        sheet["G2"] = "n"
    wbC.save(COMPETITORS_DATABASE_LOCATION)


def main_screen():
    global winners_visibility_button_color
    winners_visibility_button_color = check_winners_visibility()
    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x600")
    main_screen.title("Manager Page")
    Label(text="Choose one of the options bellow", bg="blue", fg="white", width="300", height="1", font=("Calibri", 15)).pack()
    Label(text="").pack()
    Button(text="Add Competitor", height="2", width="30", command=add_competitor).pack()
    Label(text="").pack()
    Button(text="Add Student", height="2", width="30", command=add_student).pack()
    Label(text="").pack()
    Button(text="Competitors Table", height="2", width="30", command=competitors_table).pack()
    Label(text="").pack()
    Button(text="Students Table", height="2", width="30", command=students_table).pack()
    Label(text="").pack()
    global winners_visibility_button
    winners_visibility_button = Button(text="Winners Visibility", bg=winners_visibility_button_color, height="2", width="30", command=set_winners_visibility)
    winners_visibility_button.pack()

    main_screen.mainloop()


main_screen()
