import pandas as pd
import openpyxl

COMPETITORS_DATABASE_LOCATION = 'C:/School App Project/competitors database.xlsx'
STUDENTS_DATABASE_LOCATION = 'C:/School App Project/students database.xlsx'


def find_winner_from_class(class_to_check, competitor_data):
    counter = 1
    votes_max_number = 0
    winner = competitor_data[0]
    for competitor in competitor_data:
        if str(competitor[3]) == class_to_check:
            if str(winner[3]) != class_to_check:
                winner = competitor
            if competitor[2] >= winner[2]:
                winner = competitor
    return winner


def set_all_already_voted_to_n_for_testing():
    wbS = openpyxl.load_workbook(STUDENTS_DATABASE_LOCATION)
    sheet = wbS.active
    counter = 2
    while True:
        temp = 'E' + str(counter)
        AlreadyVotedCheckName = 'C' + str(counter)
        sheet[AlreadyVotedCheckName] = 'n'
        counter += 1
        if counter == 9:
            break
    wbS.save(STUDENTS_DATABASE_LOCATION)


while True:
    print("Use one of the following commands: 'COMPETITORS', 'STUDENTS', 'WINNER_FROM', 'RESET'")
    manager_request = input("Enter command: ")
    if manager_request == 'COMPETITORS':
        df = pd.read_excel(COMPETITORS_DATABASE_LOCATION)
        print(df)
    elif manager_request == 'STUDENTS':
        df = pd.read_excel(STUDENTS_DATABASE_LOCATION)
        print(df)
    elif manager_request == 'RESET':
        set_all_already_voted_to_n_for_testing()

    elif manager_request == 'WINNER_FROM':
        winner_class = input("Enter the class you want to see the who the winner is: ")
        data_in = pd.read_excel(COMPETITORS_DATABASE_LOCATION)
        df = pd.DataFrame(data_in, columns=['FirstName', 'LastName', 'VotesNumber', 'Class', 'Id'])
        data_out = df.values.tolist()
        winner_from_class = find_winner_from_class(winner_class, data_out)
        print("Winner name: " + winner_from_class[0] + " " + winner_from_class[1] + ", Winner id: " + str(winner_from_class[4]))
