students = []
for i in range(4):
    student = {}
    try:
        print("Enter information for student ("+str(i+1)+"): ")
        student['id'] = int(input("Enter ID: "))
        student['name'] = input("Enter Name: ")
        student['age'] = int(input("Enter Age: "))
        student['score'] = int(input("Enter Score: "))
        print("=" * 100)
    except:
        print("Invalid Input\nEnter information for student ("+str(i+1)+"): ")
        student['id'] = int(input("Enter ID: "))
        student['name'] = input("Enter Name: ")
        student['age'] = int(input("Enter Age: "))
        student['score'] = int(input("Enter Score: "))
        print("=" * 100)
    students.append(student)
print("\n Bellow are the students information:")
print(students)