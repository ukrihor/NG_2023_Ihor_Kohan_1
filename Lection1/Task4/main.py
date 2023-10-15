import math


def drawLine():
    print("-"*75)


drawLine()
print("Welcome to the calculator program.")
print("You can:")
print("1)Sum two numbers, use '+' to do this, and enter two numbers.\n"
"2) Subtract two numbers, use '-' for this, and enter two numbers.\n"
"3) Multiply two numbers, for this use '*', and enter two numbers\n"
"4) Divide two numbers, use '/' to do this, and enter two numbers.\n"
"5) Square root of the number, for this use '//',and enter the number\n"
"6) number to power, for this use '^', and enter the number.")
drawLine()

def func(sign):
    try:
        match sign:
            case "+":
                num_1 = int(input("Input first number: "))
                num_2 = int(input("Input second number: "))
                sum = num_1 + num_2
                print(str(num_1) + sign + str(num_2) + " =",str(sum))
            case "-":
                num_1 = int(input("Input first number: "))
                num_2 = int(input("Input second number: "))
                subt = num_1 - num_2
                print(str(num_1) + sign + str(num_2) + " =",str(subt))
            case "*":
                num_1 = int(input("Input first number: "))
                num_2 = int(input("Input second number: "))
                subt = num_1 * num_2
                print(str(num_1) + sign + str(num_2) + " =",str(subt))
            case "/":
                num_1 = int(input("Input first number: "))
                num_2 = int(input("Input second number: "))
                subt = num_1 / num_2
                print(str(num_1) + sign + str(num_2) + " =",str(subt))
            case "//":
                num_1 = int(input("Input number: "))
                square_root = math.sqrt(num_1)
                print("Square root of a "+ str(num_1) + " =",square_root)
            case "^":
                num_1 = int(input("Input number: "))
                num_2 = int(input("Input power for number: "))
                pow_num = math.pow(num_1,num_2)
                print(str(num_1) +sign + str(num_2) +" =",pow_num)
            case _:
                raise ValueError("enter another character")
    except ValueError as e:
        print(f"Error: {e}")


func(input("Input sign: "))
        
