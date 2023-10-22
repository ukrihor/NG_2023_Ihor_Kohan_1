def menu():
    print("-"*40)
    print("Temperature Conversion Program")
    print("Choose an option:")
    print("1) Convert from Celsius to Fahrenheit")
    print("2) Convert from Fahrenheit to Celsius")
    print("-"*40)

def celsius_to_fahrenheit(celsius):
    return (9/5 * celsius + 32)

def fahrenheit_to_celsius(fahrenheit):
    return (32 - fahrenheit) * 5/9

menu()
choice = input("Enter the option number (1/2): ")

if choice == "1":
    celsius = float(input("Enter the temperature in degrees Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius = {fahrenheit} degrees Fahrenheit")
elif choice == "2":
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit = {celsius} degrees Celsius")
else:
    print("Invalid choice. Please enter 1 or 2.")
