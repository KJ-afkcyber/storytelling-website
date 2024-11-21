#welcome our users
print ("Welcome to our nature walks center.What would you like to do?")
#set an initial choices value
choices = ''
#start a loop until the user presses q to quit
while choices != 'q':
    #display all choices
    print ("[1]Enter 1 to go cycling \n")
    print ("[2]Enter 2 to go for a run \n")
    print ("[3]Enter 3 to go for mountain climbing \n")
    print ("[q]Enter q to quit")
#ask for the choices
    choices = int(input("What would you like to do?"))
#check choices
    if choices == 1:
        print("Here is a bycycle , Have fun!")
    elif choices == 2:
        print("Here are some running shoes, Enjoy!")
    elif choices == 3:
        print("Here is a map, Good luck!")
    elif choices == 'q':
        print("Thanks for stopping by, Have a good day!")
    else:
        print("I dont under stand that choice, please try again")
#print a message that we are all finished
print("Thanks again,bye now.")                 