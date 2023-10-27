input_string = input("Enter a string: ")

input_string = input_string.lower()

vowels = ""

# Identify the vowels
for char in input_string:
    if char in "aeiou":
        vowels += char + " "

print("Vowels in the string:", vowels)

