# student_details=[]
# student_info={}

# # Ask student to enter details
# for i in range(1):
#     print(f"Enter student ({i+1})")

#     id =int(input("ID: "))
#     name=input("Name: ")
#     matric_no=input("Matric No: ")
#     department=input("Department: ")

# #Accept the list to dictionary
# students= {
#     "id": id,
#     "name":name,
#     "matric_no": matric_no,
#     "department": department

# }
# student_details.append(students)
# student_info=student_details

# file=open('week2/file3.txt','w')

# file.writelines(students)
# file.close()
# print( 'The data created successful')


file = open('week3/student.txt', 'a')
file.write('ID, NAME, MATRIC NUMBER, AGE\n')
for i in range(2):
    print(f'Enter info for student {i+1}')
    name = input('Enter Name: ')
    matric = input('Enter Matric No: ')
    age = input('Enter Age: ')

    file.write(f'{i+1}, {name}, {matric}, {age}\n')
    print('='*100)
file.close()