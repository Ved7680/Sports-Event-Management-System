def New_User():

    name = input("Enter your name          : ")
    en_num = input("Enter Enrollment No    : ")
    date = input("Enter date of joining    : ")
    program = input("Enter enrolled program: ")

    log_id = input("Enter new login ID: ")
    pass_word = input("Enter password : ")
    con_pass = input("Confirm Password: ")

    new_user = open("Users.txt", mode="a+")
    new_user.write("""Name              : %s\r\n"""%name)
    new_user.write("""Enrollment No.    : %s\r\n"""%en_num)
    new_user.write("""Date of joining   : %s\r\n"""%date)
    new_user.write("""Program of student: %s\r\n"""%program)

    
    if(pass_word == con_pass):
        new_user.write("""Login ID: %s\r\n"""%log_id)
        new_user.write("""Password: %s\r\n"""%pass_word)
        print("Details Saved")
    else:
        print("Renter Password")

newuser = New_User()

    
    
    
