
# Initialize an empty list and dictionary
mydatabase = []
mydatabase2 = {}

# Get student details
for i in range(2):
    print(f"Enter your student ({i + 1}): ")
    student_id = int(input("ID: "))
    name = input("Name: ")
    matric_no = input("Matric No: ")
    age = int(input("age: "))
    department=input("Department: ")

    # Store student details in a dictionary
    student_details = {
        "id": student_id,
        "name": name,
        "matric_no": matric_no,
        "age": age,
        "department": department
    }
    
    # Append dictionary to list
    mydatabase.append(student_details)

    # Update mydatabase2 with student details
    mydatabase2 = mydatabase
# Define the ID to delete

print("\n All student Details:")
print(*mydatabase2, sep="\n")
print("="*100)
# print(*mydatabase2, sep="\n")
# READ
#PROGRAM THAT REMOVE DATA USING ID
idvalue=int(input("Enter id to be deleted: "))
filterDeleteId=list(filter(lambda x: x["id"]!=idvalue, mydatabase2))

print("Left Data after deletion")
print(*filterDeleteId, sep="\n")

# UPDATE
item=input("Enter name from the id: ")
def checkId(item):
    item['name'] = 'Faniran Moshood Abiola' if item['id'] == 1 else item['name']
    return item
updateData = list(map(lambda item: checkId(item), mydatabase2))

print(*updateData, sep='\n')

