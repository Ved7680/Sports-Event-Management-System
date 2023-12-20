def Main_Menu():
    print("""******************************************************
                        Main Menu
                    1. Organize Event
                    2. Achiievements
                    3. Budget
                    4. Event Timetable
                    5. Exit
    ******************************************************""")

    choice = int(input("Please Enter your choice: "))

    if choice == 1:
        organize = Org_Event()
                     
        players = int(input("Enter no. of players you want to add: "))
        play = Players(players)         

    if choice == 2:
        ach = Achievements()

    if choice == 3:
        evt_bud == Budget()

    if choice == 4:
        evt_table = Evt_Time_Table()

    if choice == 5:
        sure = input("Are you sure to want to exit (Y/N): ")
        if sure =="y" or sure =="Y":
            print("Thanks for visiting")
