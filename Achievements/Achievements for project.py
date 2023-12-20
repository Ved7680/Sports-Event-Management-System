def Achievements():

    print("Welcome to Achievements Section")
    print("""Main Menu
1. Add Achievemnt
2. View Achievements
3. Exit""")

    ach_choice = int(input("""Enter your choice: """))

    if ach_choice == 1:
        ach_file = open("Achievements.txt",mode = "a+")
        add_ach = input("Enter the achievement below:\n")

        ach_file.write("""%s\r\n"""%add_ach)
        ach_file.close()

        return ach_file

    if ach_choice == 2:
        ach_r = open("Achievements.txt",mode = "r")
        print(ach_r.read())

    if ach_choice == 3:
        print("Thanks for visiting")


achievements = Achievements()
        
    
