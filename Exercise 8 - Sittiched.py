usernameInput = input("username:  ")
passwordInput = input("password:  ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Welcome to program")
    print("What is your order?")
    print("1) Iphone (20000 baht per each)")
    print("2) Ipad (15000 baht per each)")
    orderInput = int(input(">>"))
    if orderInput == 1:
        print("how many IPHONE you want to order?")
        numOrder = int(input(">>"))
        print(25000*numOrder, "baht")
    if orderInput == 2:
        print("how many IPAD you want to order?")
        numOrder = int(input(">>"))
        print(15000*numOrder, "baht")
