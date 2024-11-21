def calculator():
    #this will be our calculator functions
    owner = "Jeniffer's"
    print("Welcome to "+owner+"Calculator program")

    print("Select operation")
    print("1 - Addition")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")





    while True:
        #get user input
        choice =input("Enter choice(1/2/3/4) \n")

        num1 = float(input("Enter the first number \n"))
        num2 = float(input("Enter the second number \n"))

        if choice == '1':
            print(num1, "+",num2,"=",num1+num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1-num2)

        elif choice == '3':
            print(num1, "*", num2, "=", num1*num2)

        elif choice == '4':
            if num2 == 0:
                print("Error division by 0")
            else:
                print(num1,"/", num2, "=", num1/num2)

        break
    else:
        print("invalid input-")                      


            




calculator()    
