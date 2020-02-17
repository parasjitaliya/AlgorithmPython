from utilitylogic import generallogic
obj = generallogic()

print("Enter 1 for Celcius to Fahrenheit conversion !")
print("Enter 2 for Fahrenheit to Celcius conversion !")
while True:
    try:
        choice = int(input("Enter your choice:"))
        temp = int(input("Enter the temperature:"))
        if choice == 1 or choice == 2:
            break
        print("wrong choice!! choice should be 1 or 2")
    except:
        print("invalid input!! choice should be 1 or 2 and temperature should be a number !")

obj.conversion_of_temperature(choice,temp)