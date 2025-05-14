message=str(input("Enter your first statement: "))
print(message.capitalize())
print(message.lower())
print(message.title())
print(message.upper())
message1=str(input("Enter any string from the first statement"))
# if message1 != message.find(message1):
print("The position of your string is: ", message.find(message1))
print("The total number of the occurence is: ", message.count(message1))
# else:
#     print("Out of range")