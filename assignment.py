# Changing turple value in a sequence of data
int_valve= (1, 2, 3, 4, 5, 5)
# Let convert tuple to list
int_valve= list(int_valve)
int_valve[2] = 8
print(int_valve)


# Creating variable that consist of first name, Surname and Last Name and should be printed on the same line 


# line separated by space
first_name = "Moshood"
surname="Faniran"
middle_name="Abiola"

print(surname + "", first_name + "", middle_name + "") 



# Write a python  to display "I love python Language"
subject="I love python language \n" * 1000
print(subject)



# Creating turple data and print it out
name = ("Moshood", "Abiola", "ishola", "Faniran",
        "Afeez",)
subject = ("Mathematic", "Physis", "Chemistry", "Biology", "Agric Science")
print(name,"\n", subject, "\n")



# Used range to generate a sequence of Number from 1 to 200
for number in range(1,200):
    print(number, end=" ""\n")