info1=[ ]
info2= [ ]
info3 = [ ]
info4=[ ]
info5= [ ]
info6 = [ ]
info7=[ ]
info8= [ ]
info9 = [ ]
info10=[ ]

try:
        print('Enter the first Info')
        student1=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info1.append(student1)
except:
        print("Invalid Input, Enter the correct value")
        student1=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info1.append(student1)
try:
        print('Enter the Second Info')
        student2=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info2.append(student2)
except:
        print("Invalid Input, Enter the correct value")
        student2=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info2.append(student2)
try:
        print('Enter the Third Info')
        student3=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info3.append(student3)
except:
        print("Invalid Input, Enter the correct value")
        student3=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info3.append(student3)
            
try:
        print('Enter the forth Info')
        student4=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info4.append(student4)
except:
        print("Invalid Input, Enter the correct value")
        student4=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info4.append(student4)
try:
        print('Enter the fifth Info')  
        student5=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info5.append(student5)
except:
        print("Invalid Input, Enter the correct value")
        student5=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info5.append(student5)
try:    
        print('Enter the sixth Info')
        student6=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info6.append(student6)
except:
        print("Invalid Input, Enter the correct value")
        student6=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info6.append(student6)
try:   
        print('Enter the Seventh Info')
        student7=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info7.append(student7)
except:
        print("Invalid Input, Enter the correct value")
        student7=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info7.append(student7)
try:  
        print('Enter the Eighth Info')
        student8=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info8.append(student8)
except:
        print("Invalid Input, Enter the correct value")
        student8=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info8.append(student8)
try:
        print('Enter the Nineth Info')
        student9=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info9.append(student9)
except:
        print("Invalid Input, Enter the correct value")
        student9=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info9.append(student9)
try:
        print('Enter the Tenth Info')
        student10=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info10.append(student10)
except:
        print("Invalid Input, Enter the correct value")
        student10=int(input('id: ')), str(input('name: ')), int(input('age: ')), int(input('score: '))
        info10.append(student10)
    
print("The list of all the store information are below ")

print('The first student information is: ', info1)
print('The Second student information is: ', info2)
print('The Third student information is: ', info3)
print('The Forth student information is: ', info4)
print('The Fifth student information is: ', info5)
print('The Sixth student information is: ', info6)
print('The Seventh student information is: ', info7)
print('The Eighth student information is: ', info8)
print('The Nineth student information is: ', info9)
print('The Tenth student information is: ', info10)
    
    # info1={id: " ", name:" ", }
# except:
#     print("Invalid Input, Enter the correct value")


age=[ ]
name= [ ]
score=[ ]
id=[ ]
for i in range(10):
    msg= (print("Enter the statement (" + str(i+1)+"): "))
    try:    
        store1=int(input("id: ") )
    except:
        print('Invalid Input, Enter the correct value')
        store1=int(input("id: ") )
    try: 
        store2=str(input("name: ") )
    except:
        print('Invalid Input, Enter the correct value')
        store2=str(input("name: ") )
    try:
        store3=int(input("age: ") )
    except:
        print('Invalid Input, Enter the correct value')
        store3=int(input("age: ") )
    try:
        store4=int(input("score: ") )
    except:
        print('Invalid Input, Enter the correct value')
        store4=int(input("score: ") )
score.append(store4)
age.append(store3)
name.append(store2)
id.append(store1)

# Displaying Result on the screen
 
print(id, name, age, score )
i+=1