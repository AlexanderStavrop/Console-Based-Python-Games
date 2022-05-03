def fill_dict(lns, dict):
    for i in lns:
        values = ''
        single_line = i.split()
        key = str(single_line[0])

        for j in range(1, len(single_line)):
            if j == 1:
                values = single_line[j]
            else:
                values = values + "," + single_line[j]
        dict[key] = values

def combine_teams(dict):
    first = None
    to_pop = []
    for key in dict:
        students = str(dict[key])
        if len(students.split(",")) == 1 and first is None:
            first = key
        elif len(students.split(",")) == 1:
            single = students.split(",")
            values = dict[first] + "," + single[0]
            dict[first] = values
            to_pop.append(key)
            first = None

    for i in to_pop:
        dict.pop(i)

    # for i in dict:
    #     print(dict[i])

def print_write_teams(dict):
    file = open("outputTeams.txt", "w")

    for i in dict:
        file.write(i + " : " + dict[i] + "\n")
        print(i + " : " + dict[i])
    file.close()

def find_specific_team(dict):
    name = input("Enter the name of the team you want to find: ")

    for i in dict:
        if i == name:
            print("\nTeam: " + name + "\nMembers: " + dict[i])
            break
    else:
        print("\nCouldn't find a team with the name '" + name + "'")

def find_specific_student(dict):
    user_input = input("Enter the AM of the student you want to find: ")
    found = False

    for i in dict:
        if not found:
            values = str(dict[i])
            names = values.split(",")
            for j in range(0, len(names)):
                if user_input == names[j]:
                    print("\nTeam: " + i + "\nMembers: " + dict[i])
                    found = True
                    break
        else:
            break

    if not found:
        print("\nCouldn't find a student with the AM '" + user_input + "'")

def menu():
    valid = False
    choice = 0

    while choice != 5:
        while not valid:
            print()
            print("#####################Main Menu#####################")
            print("1.Combine two teams................................")
            print("2.Print teams......................................")
            print("3.Find specific team...............................")
            print("4.Find specific student............................")
            print("5.Exit.............................................")
            try:
                choice = int(input("\nYour answer: "))
                if not 0 < choice < 6:
                    raise ValueError
                else:
                    valid = True
            except (TypeError, NameError, ValueError):
                print("\nInvalid input!!!!\nPlease try again")


        if choice == 1:
            combine_teams(lab_info)
        elif choice == 2:
            print_write_teams(lab_info)
        elif choice == 3:
            find_specific_team(lab_info)
        elif choice == 4:
            find_specific_student(lab_info)
        else:
            break

        valid = False
        choice = 0

if __name__ == "__main__":
    teams = open("students.txt")
    lab_info = {}

    lines = teams.readlines()
    fill_dict(lines, lab_info)
    menu()
    teams.close()
