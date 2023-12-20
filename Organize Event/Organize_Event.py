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

og_evt = Org_Event()
a = int(input("                 Enter no. of players: "))
play_evt = Players(a)
