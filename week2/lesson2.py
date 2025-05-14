import os

# file = open('week2/file2.txt', '')
# for i in range(10, 20):
#     file.write(f'{i+1} Today is Thursday\n')

# file.close()
# filename = 'week2/file1.txt'
# with open(filename, 'r') as file:
#     print(file.read())
# file.close()

# os.removedirs('week2/ade')

# print(os.mkdir('week2/ade'))

def createFile(location, name):
    if not os.path.isdir(location):
        os.mkdir(location)
    file = open(location + '/' + name, 'x')
    file.close()


# createFile('week3', 'StudentsFile.txt')
print(os.listdir('week3'))
# os.removedirs('week3')