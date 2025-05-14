# Program to generate prime number from 2 to 100

for num in range(2, 101):
    check_prime = 0
    for div in range(1, num + 1):
        if num % div == 0:
            check_prime += 1
    if check_prime == 2:
        print(num)