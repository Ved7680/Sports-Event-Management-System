# Author: Ved J Nayi
# Enrollment No. : AU2140055
# Project Topic : Event Management System

def Org_Event():
    sprt = input("""*******************************************************
                Enter name of sport: \n""")
    ven = input("             Enter venue for your event: \n")
    date = input("                 Enter date of event: \n")
    time = float(input("    Enter time of event(Acc. to 24 hour system): \n"))
    print("*******************************************************")

    org_evt = open("Organize_Event.txt",mode='a+')
    org_evt.write("Sport: %s\r\n"%sprt)
    org_evt.write("Venue: %s\r\n"%ven)
    org_evt.write("Date : %s\r\n"%date)  
    org_evt.write("Time : %0.2f\r\n"%time)

def Players(n):
    for i in range(1,n+1):
        play = open('Organize_Event.txt',mode='a+')
        play3 = input("""*******************************************************
            Enter Name of Player: """)
        play.write("Name: %s\r\n"%play3)
        e_num3 = input("""
        Enter Enrollment No. of the player: """)
        print("*******************************************************")
        play.write("Enrollment No.: %s\r\n"%e_num3)


def Achievements():

    print("Welcome to Achievements Section")
    print("""*******************************************************
                        Main Menu
                        1. Add Achievemnt
                        2. View Achievements
                        3. Exit
*******************************************************""")

    ach_choice = int(input("""Enter your choice: """))

    if ach_choice == 1:
        ach_file = open("Achievements.txt",mode = "a+")
        add_ach = input("Enter the achievement below:\n")

        ach_file.write("""%s\r\n"""%add_ach)
        print("Achievement Added")
        ach_file.close()

        return ach_file

    if ach_choice == 2:
        ach_r = open("Achievements.txt",mode = "r")
        print(ach_r.read())

    if ach_choice == 3:
        print("Thanks for visiting")


def Budget():
    det_bud = input("""*******************************************************
        Enter detailed budget below: \n""")
    bud = open('Budget.txt',mode='a+')
    bud.write("""%s\r\n"""%det_bud)
    print(bud.read())
    bud.close()


def Evt_Time_Table():
    evt_time = open('Organize_Event.txt',mode='r')
    print(evt_time.read())
    evt_time.close()


def New_User():

    name = input("Enter your name          : ")
    en_num = input("Enter Enrollment No      : ")
    date = input("Enter date of joining    : ")
    program = input("Enter enrolled program  : ")

    log_id = input("Enter new login ID: ")
    pass_word = input("Enter password    : ")
    con_pass = input("Confirm Password  : ")

    new_user = open("Users.txt", mode="a+")
    new_user.write("""Name              : %s\r\n"""%name)
    new_user.write("""Enrollment No.    : %s\r\n"""%en_num)
    new_user.write("""Date of joining   : %s\r\n"""%date)
    new_user.write("""Program of student: %s\r\n"""%program)

    
    if(pass_word == con_pass):
        new_user.write("""Login ID: %s\r\n"""%log_id)
        new_user.write("""Password: %s\r\n"""%pass_word)
        print("Details Saved")
        Main_Menu();
    else:
        print("Renter Password")


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

        m_menu = Main_Menu()

    if choice == 2:
        ach = Achievements()
        m_menu = Main_Menu()

    if choice == 3:
        evt_bud = Budget()
        m_menu = Main_Menu()

    if choice == 4:
        evt_table = Evt_Time_Table()
        m_menu = Main_Menu()

    if choice == 5:
        sure = input("Are you sure to want to exit (Y/N): ")
        if sure =="y" or sure =="Y":
            print("Thanks for visiting")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------#

print("""******************************************************
         Welcome to Sports Management System
******************************************************""")

new = input("         Are you an new user(Y/N): ")

if new =="Y" or new =="y":
    New_User();
elif new =="n" or new == "N":
    cred1 = input("                Enter Login ID: ")

    print("""******************************************************""")

    cred2 = input("                Enter Password: ")


    if (cred1 == "Sports_Sec" and cred2 == "sp_sec") or (cred1 == "Sports_Mem" and cred2 == "sp_mem") or (cred1 == "guest" and cred2 == "guest"):
        print("""******************************************************
                     Login Successful
    ******************************************************""")
        main_menu = Main_Menu()
        
    else:
        print("""************************************************
              Invalid Login ID or Password
    ************************************************""")

else:
    print("Both are passwords are not same")
