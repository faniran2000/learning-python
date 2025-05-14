# for n in range(1, 101):
#     print(n)
#     if n == 30:
#         break

# for n in range(1, 101):
#     if n >=20 and n <=40:
#         continue
#     print(n)

# scores = [20, 43, 32, 50]
# for score in scores:
#     print(score)

# msg = 'Hello World'
# for m in msg:
#     print(m)

# student_info = {'name': 'Ade', 'matricno': 'HC20240102924', 'gender': 'Male'}
# for student, info in student_info.items():
#     print(student, info, sep=': ')
#     if student == 'matricno': 
#         continue
# else:
#     print('Loop end')

# initial
# while condition:
    # body of the loop 
    # increment/decrement

# run = True
# count = 0
# while run:
#     print("I'm Programmer!")
#     if count == 10:
#         break
#     count += 1
# else:
#     print("I'm not a programmer")

# count = 0
# while True:
    # if count < 150:
    #     print("I'm Programmer!")
    # elif count < 200:
    #     print("I'm not Programmer!")
    # else:
    #     break
    # print(count)
    # count += 1

# Assign multi-value to single variable
# num = 1, 2, 3, 4, 5
# print(num)

# # Assign multi-value to multi-variables
# a, b, c, d = 1, 2, 3, 4
# print(b, c, d, a)

# # Assign single value to multi-variables
# a=b=c=d = 50
# print(b)
# print(a)

# ERROR HANDLING IN PYTHON
# try:
#     num = int(input('Enter number: '))
#     print(num)
# except:
#     print('Invalid input')
# finally:
#     print('Final block')

# STRING METHOD

name = 'adekola olu olu'
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.title())
print(name.center(50))
print('a56756756876')
print('a' * 50)
print('z7687686'.rjust(50))
print(name.rjust(50))
print(name.find('olus'))
print(name.count(' '))
name = name.replace('olu', 'Kola')
print(name)

# LIST METHOD
myList = ['Ade', 203, [1, 2, 3], True]
myList.append('OK')
myList.append([9, 8, 7])
print(myList.pop(2))
myList.extend([50,30,70])
# del myList
# myList.clear()
myList.insert(0, 'Num 1')
myList.remove('Ade')
# myList.index('Ade')
print(myList.index('Ade'))