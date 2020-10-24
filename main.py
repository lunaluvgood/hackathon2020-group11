import random
from tabulate import tabulate


def rebuildQuestionList():
    global questions
    study_subject = input("Which subject would you like to study?\n")
    pathtofile = r"questions/"+study_subject+".txt"
    unsorted_questions = []
    questions = []
    num_lines = 0
    with open(pathtofile, 'r') as f:
        unsorted_questions = f.readlines()
    unsorted_questions = [i.strip() for i in unsorted_questions]
    with open(pathtofile, 'r') as f:
        for i, l in enumerate(f):
            num_lines = i + 1
    for i in range(int(num_lines / 2)):
        questions.append([])
    line_num = 0
    for i in range(0, len(questions)):
        for i1 in range(2):
            questions[i].append(unsorted_questions[line_num])
            line_num += 1


def ask_questions():
    limit = len(questions)
    print("\n")
    score = 0
    asked = shuffle(questions)
    for i in range(len(asked)):
        print(asked[i][0] + "\n")
        if input("Answer:\n") == asked[i][1]:
            print("CORRECT: The answer was properly entered and is correct\n")
            score = score + 1
        else:
            print(
                "INCORRECT: The answer is either not correct or was not properly entered\n")
            print("The correct answer was:\n" + asked[i][1] + "\n")
            print(
                "Press ENTER to continue to the next question\nOR\nInput 'c' if you think you were correct\n")
            if input() == "c":
                score = score + 1

    print("You got " + str(score) + "/" + str(limit) + " answers correct.")


def shuffle(list_to_shuffle):
    l = len(list_to_shuffle)
    shuffledList = []
    for i in range(0, l):
        index = random.randint(0, len(list_to_shuffle)-1)
        itemToShuffle = list_to_shuffle[index]
        shuffledList.append(itemToShuffle)
        list_to_shuffle.remove(list_to_shuffle[index])
    return shuffledList


def run_ask_questions():
    running = 'y'
    rebuildQuestionList()
    while running == 'y':
        ask_questions()
        correct_input = 0
        while correct_input == 0:
            cont = input(
                "Would you like to continue studying?\n\ny - continue studying\nn - stop studying\n\n")
            if cont == 'y':
                rebuildQuestionList()
                correct_input = 1
            elif cont == 'n':
                running = 'n'
                correct_input = 1
            else:
                correct_input = 0
    home()


def todo():
    z = bool(True)
    print("This is the to-do list")

    with open("to-do-list.txt", "r") as f:
        todoAsList = f.readlines()
        for i in range(len(todoAsList)):
            string = todoAsList[i]
            string = string[1: -1]
            list1 = string.split(", ")
            todoAsList[i] = list1
    for i in range(len(todoAsList)-1):
        todoAsList[i][-1] = todoAsList[i][-1][0:-1]
    for i in range(len(todoAsList)):
        print(todoAsList[i])
    print("\nType in what you need to do")
    x = input()
    print("When is the deadline? Example:(1 Jun 2020)")
    y = input()
    print("How is this imporant (1-5)")
    v = input()
    checker = ""
    text_file = open("to-do-list.txt", "r")
    for char in text_file:
        checker = char
    if len(checker) > 0:
        checker = checker
    else:
        checker = "Invalid"
    if checker[0] == "[":
        table = "\n" + "[" + x + ", " + y + ", " + v + "]"
    else:
        table = "[" + x + ", " + y + ", " + v + "]"
    text_file.close()

    while z == bool(True):
        print("Would you like to continue adding?(Y/N)")
        an = input()
        if an == "Y" or an == "y":
            z = bool(True)
            print("Type the stuff that you want to add to the to-do list")
            a = input()
            print("When is the deadline?")
            b = input()
            print("How important is this (1-5)")
            c = input()
            table += "\n" + "[" + a + ", " + b + ", " + c + "]"
        else:
            z = bool(False)
            print("ending")
    text_file = open("to-do-list.txt", "a")
    text_file.write(table)
    text_file.close()
    home()


def studyingSub():
    z = bool(True)
    print("Which subject would you like to study?")
    x = input("Subject: ")
    y = r"questions/" + x + ".txt"
    print(y)
    print("Question: ")
    qu = input()
    print("Answer: ")
    an = input()
    table = qu + "\n" + an
    while z == (True):

        print("Would you like to continue? (y/n)")
        con = input()
        if con == "y" or con == "Y":
            z = (True)
            print("Question: ")
            qu = input()
            print("Answer: ")
            an = input()
            table += "\n" + qu + "\n" + an
        else:
            z = (False)

    text_file = open(y, "w")
    text_file.write(table)
    text_file.close()
    home()


def sort():
    with open("to-do-list.txt", 'r') as f:
        todoAsList = f.readlines()
        for i in range(len(todoAsList)):
            string = todoAsList[i]
            string = string[1: -1]
            list1 = string.split(", ")
            todoAsList[i] = list1
    for i in range(len(todoAsList)-1):
        todoAsList[i][-1] = todoAsList[i][-1][0:-1]

    if len(todoAsList) > 1:
        for i in range(len(todoAsList)):
            j = 0
            for j in range(len(todoAsList) - 1):
                if todoAsList[j][2] > todoAsList[j+1][2]:
                    todoAsList[j], todoAsList[j +
                                              1] = todoAsList[j+1], todoAsList[j]
                j += 1
        for i in range(len(todoAsList) - 1, -1, -1):
            print(todoAsList[i][0] + ", " + todoAsList[i]
                  [1] + ", " + todoAsList[i][2])
    else:
        print(todoAsList)
    home()


def clear_todo():
    with open("to-do-list.txt", "w") as f:
        pass
    home()


def delete_item():
    with open("to-do-list.txt", "r") as f:
        todoAsList = f.readlines()
        for i in range(len(todoAsList)):
            string = todoAsList[i]
            string = string[1: -1]
            list1 = string.split(", ")
            todoAsList[i] = list1
    for i in range(len(todoAsList)-1):
        todoAsList[i][-1] = todoAsList[i][-1][0:-1]
    for i in range(len(todoAsList)):
        print(todoAsList[i])
    item = int(input(
        "Which item would you like to delete? (1-"+str(len(todoAsList))+")\n"))
    del(todoAsList[item-1])
    with open("to-do-list.txt", "w") as f:
        pass
    for i in range(len(todoAsList)):
        z = bool(True)
        x = todoAsList[i][0]
        y = todoAsList[i][1]
        v = todoAsList[i][2]
        checker = ""
        text_file = open("to-do-list.txt", "r")
        for char in text_file:
            checker = char
        if len(checker) > 0:
            checker = checker
        else:
            checker = "Invalid"
        if checker[0] == "[":
            table = "\n" + "[" + x + ", " + y + ", " + v + "]"
        else:
            table = "[" + x + ", " + y + ", " + v + "]"
        text_file.close()
        text_file = open("to-do-list.txt", "a")
        text_file.write(table)
        text_file.close()
    home()


def edit_item():
    with open("to-do-list.txt", "r") as f:
        todoAsList = f.readlines()
        for i in range(len(todoAsList)):
            string = todoAsList[i]
            string = string[1: -1]
            list1 = string.split(", ")
            todoAsList[i] = list1
    for i in range(len(todoAsList)-1):
        todoAsList[i][-1] = todoAsList[i][-1][0:-1]
    for i in range(len(todoAsList)):
        print(todoAsList[i])
    item = int(input(
        "Which item would you like to edit? (1-"+str(len(todoAsList))+")\n"))
    print("Editing\n" + str(todoAsList[item-1]) + "\n")
    correct_input = 0
    while correct_input == 0:
        spec_item = input(
            "What would you like to edit? \nt - title\nd - date\ni - importance\n")
        if spec_item == 't':
            todoAsList[item-1][0] = input("Enter new value: ")
            correct_input = 1
        elif spec_item == 'd':
            todoAsList[item-1][1] = input("Enter new value: ")
            correct_input = 1
        elif spec_item == 'i':
            todoAsList[item-1][2] = input("Enter new value: ")
            correct_input = 1
        else:
            print("Wrong input")
    with open("to-do-list.txt", "w") as f:
        pass
    for i in range(len(todoAsList)):
        z = bool(True)
        x = todoAsList[i][0]
        y = todoAsList[i][1]
        v = todoAsList[i][2]
        checker = ""
        text_file = open("to-do-list.txt", "r")
        for char in text_file:
            checker = char
        if len(checker) > 0:
            checker = checker
        else:
            checker = "Invalid"
        if checker[0] == "[":
            table = "\n" + "[" + x + ", " + y + ", " + v + "]"
        else:
            table = "[" + x + ", " + y + ", " + v + "]"
        text_file.close()
        text_file = open("to-do-list.txt", "a")
        text_file.write(table)
        text_file.close()
    home()


def GPACalculator():
    gradesLst = []
    classes = int(input("How many classes do you have? "))
    for i in range(1, classes+1):
        grades = input("What grade do you have for class " + str(i) +
                       ". Please Enter a Letter Grade Ex. if you have 90 through 100 type: A? ")
        if grades == "A" or grades == "a":
            gradesLst.append(4)
        elif grades == "B" or grades == "b":
            gradesLst.append(3)
        elif grades == "C" or grades == "c":
            gradesLst.append(2)
        elif grades == "D" or grades == "d":
            gradesLst.append(1)
        elif grades == "F" or grades == "f":
            gradesLst.append(0)
        else:
            print("Invalid responce. Try Again")
            GPACalculator()

    total = sum(gradesLst) / classes
    print("GPA: " + str(total))
    again = input("Would you like to try again? (Y/N) ")
    if again == "Y" or again == "y":
        GPACalculator()
    home()

def create_schedule():
    print("Create the schedule (If you don't have classes on the period put no)")
    first = input("Write 1st period subject: ")
    second = input("Write 2nd period subject: ")
    third = input("Write 3rd period subject: ")
    fourth = input("Write 4th period subject: ")
    fifth = input("Write 5th period subject: ")
    sixth = input("Write 6th period subject: ")
    seventh = input("Write 7th period subject: ")
    if first == "no":
        first = "Off period"
    if second == "no":
        second = "Off period"
    if third == "no":
        third = "Off period"
    if fourth == "no":
        fourth = "Off period"
    if fifth == "no":
        fifth = "Off period"
    if sixth == "no":
        sixth = "Off period"
    if seventh == "no":
        seventh = "Off period"
    print("Put your teachers name (If you don't have classes on the period leave it empty )")
    firstT = input("Write 1st period teacher: ")
    secondT = input("Write 2nd period teacher: ")
    thirdT = input("Write 3rd period teacher: ")
    fourthT = input("Write 4th period teacher: ")
    fifthT = input("Write 5th period teacher: ")
    sixthT = input("Write 6th period teacher: ")
    seventhT = input("Write 7th period teacher: ")

    tableO = [["7:40~ 8:50", first, firstT]]
    tableO += [["8:50~ 9:00", "Break", ""]]
    tableO += [["9:00~ 10:10", third, thirdT]]
    tableO += [["10:10~ 10:40", "Tutorial", ""]]
    tableO += [["10:40~ 10:50", "Break", ""]]
    tableO += [["10:50~ 12:00", fifth, fifthT]]
    tableO += [["12:00~ 1:00", "Lunch", ""]]
    tableO += [["1:00~ 2:10", seventh, seventhT]]
    tableO += [["2:10~ 2:40", "Tutorial", ""]]

    Odd = (tabulate(tableO, headers=["Time", "Subject", "Teacher"]))
    text_file = open("Odd.txt", "w")
    text_file.write(Odd)
    text_file.close()

    tableE = [["7:40~ 8:50", "", ""]]
    tableE += [["8:50~ 9:00", "Break", ""]]
    tableE += [["9:00~ 10:10", second, secondT]]
    tableE += [["10:10~ 10:40", "Tutorial", ""]]
    tableE += [["10:40~ 10:50", "Break", ""]]
    tableE += [["10:50~ 12:00", fourth, fourthT]]
    tableE += [["12:00~ 1:00", "Lunch", ""]]
    tableE += [["1:00~ 2:10", sixth, sixthT]]
    tableE += [["2:10~ 2:40", "Tutorial", ""]]
    Even = (tabulate(tableE, headers=["Time", "Subject", "Teacher"]))
    text_file = open("Even.txt", "w")
    text_file.write(Even)
    text_file.close()
    home()


def schedule():
    print("What day is today?")
    day = input()
    if day == "Monday" or day == "Thursday":
        print("")
        text_file = open("Odd.txt", "r")
        for line in text_file:
            print(line)
    elif day == "Tuesday" or day == "Friday":
        print("")
        text_file = open("Even.txt", "r")
        for line in text_file:
            print(line)
    elif day == "Wednesday":
        print("Today is Wednesday!! You only have advisory")
    else:
        print("error")
    home()


def home():
    print("Enter the number before the task to select that task")
    print("1. Make a Study Quiz")
    print("2. Make a list of assignments")
    print("3. Calculate your GPA")
    print("4. Quit")
    wantToDo = input("What would you like to do? ")
    if wantToDo == "1":
        print("1. Create a new test")
        print("2. Take one of your tests")
        print("3. Go Back")
        wantToDo = input("What would you like to do? ")
        if wantToDo == "1":
            studyingSub()
        elif wantToDo == "2":
            run_ask_questions()
        elif wantToDo == "3":
            home()
        else:
            print("Invalid response. Try again")
    elif wantToDo == "2":
        print("1. Create a list or add to your list")
        print("2. Clear your list")
        print("3. Delete an item from your list")
        print("4. Edit an item to your list")
        print("5. Go Back")
        wantToDo = input("What would you like to do? ")
        if wantToDo == "1":
            todo()
        elif wantToDo == "2":
            clear_todo()
        elif wantToDo == "3":
            delete_item()
        elif wantToDo == "4":
            edit_item()
        elif wantToDo == "5":
            home()
        else:
            print("Invalid Input. Try again")
            home()
    elif wantToDo == "3":
        print("1. Start GPA calculator")
        print("2. Go back")
        wantToDo = input("What would you like to do? ")
        if wantToDo == "1":
            GPACalculator()
        elif wantToDo == "2":
            home()
        else:
            print("Invalid response. Try again")
            home()
    elif wantToDo == "4":
        quit

home()