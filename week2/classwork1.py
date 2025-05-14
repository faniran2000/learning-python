# PYTHON PROGRAM THAT ACCEPT 10 numbers seperated by comma from user and Find the maximu
# num=[]
# for i in range(10):
#     users=int(input("Enter number ("+ str(i + 1)+"): "))
#     total_num=num.append(users)
#     total_max=max(num)

# print(*num, sep="," )
# print(total_max)

# PYTHON PROGRAM that accept 20 number seperated by comma from the user and find the minimum number of those number
# num1 = []
# for i in range(2):
#     users=int(input("Enter number ("+ str(i + 1)+"): "))
#     total_num=num1.append(users)
#     total_min=min(num1)
# print(*num1, sep=",")
# print(total_min)

# ACCEPT THE NUMBER FROM USER SEPERATED WITH COMMA, THEN PRINT THE SUMMATION OF THOSE NUMBER
# num2=[]
# for i in range(2):
#         user3=int(input("Enter number (" + str(i +1)+"): "))
#         total_number=num2.append(user3)
    
#         total_sum= sum(num2)
# print('The total numbers accepted seperately with comma: ', end=''  )
# print(*num2, sep=", ")
# print('The total sum is: ', total_sum)

num = input('Enter 10 numbers seperated by comma: ').split(',')
print(num)
maxNum = max(num)
minNum = min(num)
sumNum = sum(map(float, num))
print(maxNum, minNum, sumNum, sep='\n')