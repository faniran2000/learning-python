'''
lambda param(s): expression
'''

# square = lambda num: num ** 2

scores = [30, 32, 39, 27, 29, 33, 40, 45, 21, 25]
# newScores = []
# for add in scores:
#     newScores.append(add + 20)
# print(scores, newScores, sep="\n")

# def add20(num):
#     return num + 20

# newScores = list(map(add20, scores))
# newScores = list(map(lambda num: num+20, scores))
# evenScores = list(filter(lambda num: num % 2 == 0, newScores))
# oddScores = list(filter(lambda num: num % 2 != 0, newScores))
# print(scores, newScores, evenScores, oddScores, sep='\n')

mydb = [
    {'id': 1, 'name': 'Oluwatobi Saka', 'gender': 'Male', 'age': 17},
    {'id': 2, 'name': 'Oluwatobi Saka', 'gender': 'Male', 'age': 17},
    {'id': 3, 'name': 'Oluwatobi Saka', 'gender': 'Male', 'age': 17},
    {'id': 4, 'name': 'Oluwatobi Saka', 'gender': 'Male', 'age': 17}
]

# CRUD OPERATION
# CREATE
newData = {}
newData['id'] = len(mydb) + 1
newData['name'] = 'Fasola Iyabo2'
newData['gender'] = 'Female'
newData['age'] = 45
mydb.append(newData)
newData = {}
newData['id'] = len(mydb) + 1
newData['name'] = 'Fasola Iyabo3'
newData['gender'] = 'Female'
newData['age'] = 45
mydb.append(newData)
newData = {}
newData['id'] = len(mydb) + 1
newData['name'] = 'Oyediran Yidiat'
newData['gender'] = 'female'
newData['age'] = 25
mydb.append(newData)
# READ
# print(*mydb, sep='\n')
filterWithAge = list(filter(lambda x: x['age'] == 17, mydb))
filterWithGender = list(filter(lambda item: item['gender'].lower() == 'female' and item['age'] < 30, mydb))
# print(*filterWithGender, sep='\n')
# UPDATE
def checkId(item):
    item['name'] = 'Abiola Moshood' if item['id'] == 4 else item['name']
    return item
updateData = list(map(lambda item: checkId(item), mydb))
# print(*updateData, sep='\n')
# DELETE
mydb = list(filter(lambda item: item['id'] != 3, mydb))
print(*mydb, sep='\n')
# print(*234, sep=' @ ')

'condition ? true statement : false statement'

'true statement if conditon else false statement'

# print(2 if 2 > 5 else 5)