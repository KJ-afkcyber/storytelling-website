#get height input from the user
height = input("Enter your height in Metres \n")

#converting the height input to integer
height = float(height)

#get weight form the user
weight = input("Enter your weight in kilogram \n")

#convert the weight to integers
weight = float(weight)

#calculate the bmi by dividing the weight with the height.The height is raised to power two.
bmi = weight / (height ** 2)

print("This is your bmi",bmi)

if(bmi<18.5):
    print("under weight")
elif(18.5 <= bmi <24 ):
    print("Normal weight")

elif (25 <= bmi < 29): 
    print("over weight")

else:
    print("obese")       