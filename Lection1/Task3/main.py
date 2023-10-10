i = 0
while i == 0:
    print("If you want to convert Celsius to Farangheit, then enter F\n" + "If you want to convert Farangheit to Celsius, then enter C")
    Choice = input("Enter (F or C): ")
    if Choice == "F":
        user_input = int(input("Input Celsius: "))
        Fahrenheit = 9/5 * user_input + 32
        print("He's Fahrenheit: ",Fahrenheit)
    elif Choice == "C":
        user_input = int(input(""))
        Celsius = 5/9 * (user_input - 32)
        rounded_Celsius = round(Celsius, 1)  
        print("He's Celsius: ",rounded_Celsius)
    else:
        print("Durak? Input F or C")