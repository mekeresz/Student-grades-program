# A student's lessons and grades can be stored in a single file. Various statistics can be presented

with open("grades.txt", "r", encoding="utf-8") as text:
    file = text.read().split()

student_data = []
# loding data from the file into dict
for line in file:

    subject, grades = line.split("-")
    grades = grades.split(",")
    grades1 = []

    for j in grades:
        if int(j) != 0:
            grades1.append(int(j))

    student_data.append({"subject": subject, "grades": grades1})


def average_list(list):

    s = sum(list)
    l = len(list)
    return round(s/l, 2)


def median_list(list):

    sorted_list = sorted(list)
    l = len(list)

    # if there are two mean values,it returns with their average
    if l % 2 == 0:
        return (sorted_list[int(l/2-0.5)]+sorted_list[int(l/2+0.5)])/2
    # otherwise with the middle number
    else:
        return sorted_list[int(l/2+0.5)]


def mode_list(list):

    sorted_list = sorted(list)
    count_grades = []

    # Counts the amount of a specific grade
    count_grades.append(sorted_list.count(1))
    count_grades.append(sorted_list.count(
        2)), count_grades.append(sorted_list.count(3))
    count_grades.append(sorted_list.count(4))
    count_grades.append(sorted_list.count(5))

    return count_grades.index(max(count_grades))+1  # which of them has the max


# In this menu option, we enter the statistics for a selected subject.
def a_func():

    print("Please choose from the following subjects:\n")
    a = 0

    # choose a curse
    while a < len(student_data):
        print(a+1, ") ", student_data[a]["subject"])
        a += 1

    while True:
        try:
            a_cho = int(input())
            # error check
            if a_cho > 0 and a_cho < len(student_data):
                # choose statistics
                print(f"Chosen subject: {student_data[a_cho-1]["subject"]}.\nCurrent grades:\n\n{student_data[a_cho-1]["grades"]}",
                      "\n\nPlease select which statistical data you are interested in\n"
                      "1) Average of grades \n2) Median of grades \n3) Mode of grades")
                break
            else:
                print("Invalid request, please choose a number from the list\n")

        except ValueError:
            print("Invalid request, please choose a number from the list\n")

    while True:
        try:
            s_cho = int(input())
            # statistic functions
            if s_cho == 1:
                print(f"Average grade of {student_data[a_cho-1]["subject"]}: ", average_list(
                    student_data[a_cho-1]["grades"]))
                break
            elif s_cho == 2:
                print(f"Median of {student_data[a_cho-1]["subject"]}: ",
                      median_list(student_data[a_cho-1]["grades"]))
                break
            elif s_cho == 3:
                print(f"Mode of {student_data[a_cho-1]["subject"]}: ",
                      mode_list(student_data[a_cho-1]["grades"]))
                break
            else:
                print("Invalid selction. Please choose a number\n")

        # error check
        except ValueError:
            print("Invalid selction. Please choose a number\n")


def b_func():
    print("Please select which statistical data you are interested in\n1) Average performance of the year \n2) Excellent performances \n3) In which subject Should I improve?")

    while True:
        try:
            selection_chosen = int(input())
            # error check
            if selection_chosen in range(1, 4):
                break
            else:
                print("Invalid selction. Please choose a number \n")
        except ValueError:
            print("Invalid selction. Please choose a number \n")

    temporary_list = []
    for index in student_data:
        temporary_list.append(average_list(index["grades"]))

    # statistic functions
    if selection_chosen == 1:
        print(f"Average of all grades: {average_list(temporary_list)}")
        if average_list(temporary_list) >= 4:
            print(f"The student is eligible for a scholarship.")
        else:
            print(f"The student is not eligible for a scholarship.")

    if selection_chosen == 2:
        # print(tant,temp,tant[temp.index(max(temp))])
        if max(temporary_list) >= 4:
            print(
                f"Excellent grade from subject {student_data[temporary_list.index(max(temporary_list))]["subject"]},well done!")
        else:
            print(
                f"Unfortunatelly there is none. Best performance: {student_data[temporary_list.index(max(temporary_list))]["subject"]}. Average: {max(temporary_list)}")

    if selection_chosen == 3:

        if min(temporary_list) <= 2:
            print(
                f"Unfortunatelly you are likely to fail {student_data[temporary_list.index(min(temporary_list))]["subject"]}.")
        else:
            print(
                f"Fortunatelly there is none. Worst performance: {student_data[temporary_list.index(min(temporary_list))]["subject"]}. Average: {min(temporary_list)}")


def c_func():

    while True:
        try:
            # choose statistics
            print(f"Please select from the following options: \n1) Add new grades to specified subject \n2) Add new subject")
            selection_chosen = int(input())

            # error check
            if selection_chosen < 1 or selection_chosen > 2:
                print("Invalid selction. Please choose a number\n")

            with open("grades.txt", "w", encoding="utf-8") as text:

                # statistic functions
                if selection_chosen == 1:

                    a = 0
                    while a < len(student_data):
                        print(a+1, ") ", student_data[a]["subject"])
                        a += 1

                    while True:

                        try:
                            option_chosen = int(input())

                            if option_chosen in range(1, len(student_data)+1):

                                print(student_data[option_chosen-1]["subject"])
                                print(
                                    f"Current grades: {student_data[option_chosen-1]["grades"]}")

                                while True:

                                    try:
                                        option_chosen2 = int(
                                            input("I would like to add this grade: \n"))

                                        if option_chosen2 in range(1, 6):
                                            student_data[option_chosen -
                                                         1]["grades"].append(option_chosen2)
                                            print(
                                                f"Added. Current grades: {student_data[option_chosen-1]["grades"]}")
                                            break

                                        else:
                                            print(
                                                f"Addition failed. Invalid grade")

                                    except ValueError:
                                        print(f"Addition failed. Invalid grade")
                                break

                            else:
                                print("Invalid value. Please choose from the list")

                        except ValueError:
                            print("Invalid value. Please choose from the list")

                if selection_chosen == 2:
                    new_subject = input("I would like to add this subject: \n")
                    student_data.append({})
                    student_data[len(student_data) -
                                 1]["subject"] = (new_subject)
                    student_data[len(student_data)-1]["grades"] = ([0])
                    print("New subject is added to the list.")

                for line in student_data:
                    text.write(f"{line["subject"]}-")

                    for i in range(0, len(line["grades"])-1):
                        if line["grades"][i] != 0:
                            text.write(f"{line["grades"][i]},")
                    text.write(f"{line["grades"][len(line["grades"])-1]}\n")
                break

        except ValueError:
            print("Invalid selction. Please choose a number\n")


def main_menu(mode):

    while True:
        try:
            return_menu = str(
                input("\nWould you like a new query? Y/N\n").upper())

            if return_menu == "Y":
                return 0
                break

            elif return_menu == "N":
                return 1
                break

            else:
                print("\nInvalid response! Please answer with Y or N.\n")

        except ValueError:
            print("\nnvalid response! Please answer with Y or N.\n")


while True:

    # Main menu
    print("Please choose one from the following options:\n\nA) Statistics for a selected subject\n\nB) Overall results\n\nC) Modify data\n")
    select_menu = input().upper()
    mode = None

    # Selcting menu A
    if select_menu == "A":
        a_func()

    # Selcting menu B
    elif select_menu == "B":
        b_func()

    # Selcting menu C
    elif select_menu == "C":
        c_func()

    else:
        print("Invalid selection. Please select a letter: A,B,or C\n")

    # return to main menu
    if main_menu(mode) == 0:
        continue
    else:
        break
