def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

user_input = int(input("Enter an integer: "))

print("Number | Divisors")

for number in range(1, user_input + 1):
    divisors = [str(i) for i in range(1, number + 1) if number % i == 0]
    divisors_str = ", ".join(divisors)
    prime_status = "prime" if is_prime(number) else "-"
    print(f"{number:<6} | {divisors_str} ({prime_status})")
