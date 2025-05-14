# #Program that stored 14 valve on a single variable

scores=(int(input("Enter the first score: ")),int(input("Enter the Second score: "))
,int(input("Enter the Third score: ")), int(input("Enter the Fouth score: ")),
int(input("Enter the Fifth score: ")),int(input("Enter the sixth score: ")),
 int(input("Enter the seventh score: ")),int(input("Enter the eighth score: ")), 
 int(input("Enter the nineth score: ")),int(input("Enter the tenth score: ")), 
 int(input("Enter the eleventh score: ")),int(input("Enter the twelveth score: ")),
 int(input("Enter the thirteenth score: ")),int(input("Enter the fourteenth score: ")),
 int(input("Enter the fiftheenth score: ")))
# #  Let convert it to list
# scores = list(scores)
# #  Printing mode 
print('Store valves are as follows: ',scores)

# Using while statement to generate  prime number between 1 and 100

# num = 1, 101
num = 2
while num < 101:  # Generate prime numbers up to 100
    is_prime = True
    num1 = 2
    while num1 * num1 <= num:
        if num % num1 == 0:
            is_prime = False
            # break
        num1 += 1
    if is_prime:
        print(num)
    num += 1

# That that accept 10 statement in one variable and print it out\

message =(str(input("Enter the statement 1: ")),str(input("Enter the Statement 2: "))
,str(input("Enter the statement 3: ")), str(input("Enter the statement 4: ")),
str(input("Enter the statement 5: ")),str(input("Enter the statement 6: ")),
 str(input("Enter the statement 7: ")),str(input("Enter the statement 8: ")), 
 str(input("Enter the statement 9: ")),str(input("Enter the tenth statement 10: ")))

print('All your statement were: ',message)
   
