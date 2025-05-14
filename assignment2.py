# Program that generate prime number in between 1 - 100
for num in range(2, 101):  # Adjusted the upper limit to include 101
    is_prime = True
    for number in range(2, int(num ** 0.5) + 1):
        if num % number == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# Program that generate even number in between 1 - 100
for num in range(2, 101, 2):
    print(num)

# Program that generate old number in between 1 - 100
for num in range(1, 101, 2):
    print(num)
# 