
print("If you want to convert Celsius to Fahrenheit, then enter F\n" + "If you want to convert Fahrenheit to Celsius, then enter C")
Choice = input("Enter (Fahrenheit or Celsius): ")
if Choice == "Fahrenheit":
    user_input = int(input("Input Celsius: "))
    Fahrenheit = 9/5 * user_input + 32
    print("He's Fahrenheit: ",Fahrenheit)
elif Choice == "Celsius":
    user_input = int(input("Input Fahrenheit: "))
    Celsius = 5/9 * (user_input - 32)
    rounded_Celsius = round(Celsius, 1)  
    print("He's Celsius: ",rounded_Celsius)
else:
    print("Error!!!\nPlease input Fahrenheit or Celsius")