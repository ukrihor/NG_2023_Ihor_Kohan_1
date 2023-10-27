
elements = []

while True:
    user_input = input("Enter an element for the list (or 'done' to finish): ")
    
    if user_input.lower() == "done":
        break  # Exit programm, if the user enters "done"
    
    elements.append(user_input)

count_of_numbers = 0


for element in elements:
    if element.isdigit():
        count_of_numbers += 1

print("The list contains {} numbers.".format(count_of_numbers))
