def Players(n):
    for i in range(1,n+1):
            play = open('Players.txt',mode='a+')
            play3 = input("""*******************************************************
                Enter Name of Player: """)
            play.write("Name: %s\r\n"%play3)
            e_num3 = input("""
           Enter Enrollment No. of the player: """)
            print("*******************************************************")
            play.write("Enrollment No.: %s\r\n"%e_num3)
            
players = Players(2)
