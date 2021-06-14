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
    add_student_screen.geometry("300x300")

    global first_name_s
    global last_name_s
    global id_s
    global class_name_s
    global first_name_entry_s
    global last_name_entry_s
    global id_entry_s
    global class_name_entry_s
    first_name_s = StringVar()
    last_name_s = StringVar()
    id_s = StringVar()
    class_name_s = StringVar()
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
    # Set Add Competitor button
    Label(add_student_screen, text="").pack()
    Button(add_student_screen, text="Add Student", width=15, height=1, bg="blue", fg="white", command=new_student_user).pack()


def new_competitor_user():
    first_name_info = str(first_name_c.get())
    last_name_info = str(last_name_c.get())
    id_info = str(id_c.get())
    class_name_info = str(class_name_c.get())
    print("Competitor{first name: " + first_name_info + ", last name: " + last_name_info + ",  id: " + id_info + ",  class name: " + class_name_info + "}")
    first_name_entry_c.delete(0, END)
    last_name_entry_c.delete(0, END)
    id_entry_c.delete(0, END)
    class_name_entry_c.delete(0, END)


def new_student_user():
    first_name_info = str(first_name_s.get())
    last_name_info = str(last_name_s.get())
    id_info = str(id_s.get())
    class_name_info = str(class_name_s.get())
    print("Student{first name: " + first_name_info + ", last name: " + last_name_info + ",  id: " + id_info + ",  class name: " + class_name_info + "}")
    first_name_entry_s.delete(0, END)
    last_name_entry_s.delete(0, END)
    id_entry_s.delete(0, END)
    class_name_entry_s.delete(0, END)


def competitors_table():
    global competitors_table_screen
    competitors_table_screen = Toplevel(main_screen)
    competitors_table_screen.title("Competitors Table Page")
    competitors_table_screen.geometry("740x300")

    # get the competitors values from the excel file
    data_in = pd.read_excel(COMPETITORS_DATABASE_LOCATION)
    df = pd.DataFrame(data_in, columns=['FirstName', 'LastName', 'VotesNumber', 'Class', 'Id', 'Picture'])
    competitors_list = df.values.tolist()

    for i in range(6):
        e = Entry(competitors_table_screen, width=20, fg='blue')
        e.grid(row=0, column=i)
        if i == 0:
            e.insert(END, 'FirstName')
        elif i == 1:
            e.insert(END, 'LastName')
        elif i == 2:
            e.insert(END, 'VotesNumber')
        elif i == 3:
            e.insert(END, 'Class')
        elif i == 4:
            e.insert(END, 'Id')
        elif i == 5:
            e.insert(END, 'Picture')

    for i in range(len(competitors_list)):
        for j in range(6):
            e = Entry(competitors_table_screen, width=20, fg='blue')
            e.grid(row=i+1, column=j)
            e.insert(END, competitors_list[i][j])


def students_table():
    global students_table_screen
    students_table_screen = Toplevel(main_screen)
    students_table_screen.title("Students Table Page")
    students_table_screen.geometry("740x300")

    # get the competitors values from the excel file
    data_in = pd.read_excel(STUDENTS_DATABASE_LOCATION)
    df = pd.DataFrame(data_in, columns=['FirstName', 'LastName', 'AlreadyVoted', 'Class', 'Id', 'PhoneNumber'])
    students_list = df.values.tolist()

    for i in range(6):
        e = Entry(students_table_screen, width=20, fg='blue')
        e.grid(row=0, column=i)
        if i == 0:
            e.insert(END, 'FirstName')
        elif i == 1:
            e.insert(END, 'LastName')
        elif i == 2:
            e.insert(END, 'AlreadyVoted')
        elif i == 3:
            e.insert(END, 'Class')
        elif i == 4:
            e.insert(END, 'Id')
        elif i == 5:
            e.insert(END, 'PhoneNumber')

    for i in range(len(students_list)):
        for j in range(6):
            e = Entry(students_table_screen, width=20, fg='blue')
            e.grid(row=i + 1, column=j)
            e.insert(END, students_list[i][j])




def main_screen():

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

    main_screen.mainloop()


main_screen()
