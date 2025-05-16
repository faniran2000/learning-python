db = []

def welcomeMsg():
    print('=' * 100)
    print('WELCOME TO OUR STUDENT MANAGEMENT SYSTEM'.center(100))
    print('=' * 100)

def options():
    print("\nAvailable Options")
    print('Enter 1 to Add Student', 'Enter 2 to Read Students', 'Enter 3 to Update Student', 'Enter 4 to Delete Student', 'Enter e to Exit\n', sep='\n')

def createStudent():
    print('Enter Student Info\n')
    student = {}
    lastId = 0 if len(db) == 0 else db[-1]['id']
    student['id'] = lastId + 1
    student['name'] = input('Enter Student Name: ')
    student['matricno'] = input('Enter Student Matric Number: ')
    student['Score'] = int(input('Enter Student Score: '))
    print('-' * 70, '\nNew Student Created Successfully!\n')
    db.append(student)

def readStudents():
    print(f'\nBelow are the info of {len(db)} Student')
    print(*db, sep='\n')

def updateStudent():
    print()
    try:
        id = int(input('Enter ID of Student to update: '))
        getStudent = list(filter(lambda s: s['id'] == id, db))
        if len(getStudent) == 0:
            print('Invalid ID')
        else:
            student = getStudent[0]
            student['name'] = input('Enter Student Name: ')
            student['matricno'] = input('Enter Student Matric Number: ')
            student['Score'] = int(input('Enter Student Score: '))
            print('-' * 70, f'\nStudent with ID ({id}) Updated Successfully!\n')
    except:
        print('Invalid ID')

def deleteStudent():
    try:
        id = int(input('Enter ID of Student to Delete: '))
        data = list(filter(lambda s: s['id'] != id, db))
        db.clear()
        db.extend(data)
        print('-' * 70, f'\nStudent with ID ({id}) Deleted Successfully!\n')
    except Exception as e:
        print(f'Invalid ID, Reason:', e)

# New change made 
welcomeMsg()
while True:
    options()
    option = input('Enter option: ')

    if option == '1':
        createStudent()
    elif option == '2':
        readStudents()
    elif option == '3':
        updateStudent()
    elif option == '4':
        deleteStudent()
    elif option.lower() == 'e':
        print('=' * 100)
        print('GOOD BYE'.center(100))
        print('=' * 100)
        break
    else:
        print(f'\n------------({option}) Invalid Option Chosen!------------\n')