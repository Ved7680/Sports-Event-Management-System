def Budget():
    det_bud = input("""*******************************************************
        Enter detailed budget below: \n""")
    bud = open('Budget.txt',mode='a+')
    bud.write("""%s\r\n"""%det_bud)
    print(bud.read())
    
budget = Budget()
