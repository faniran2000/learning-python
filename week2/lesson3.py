from os import remove

# file = open('week2/mytext.txt', 'a')
# for l in range(20, 30):
#     file.write(f'{l+1} Another sentence\n')
# file.close()

try:
    remove('week2/mytext.txt')
except:
    print('File not found!')