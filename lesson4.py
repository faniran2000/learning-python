# TUPLE METHODS
myTuple = (2,5,3,5,9,0,6,77)
print(myTuple.count(5))
print(myTuple.index(5))

# DICT METHOD
name = 'ade'
myDict = {1: 'Selim', 2: name, 3: 'Boy'}
# myDict.update({1: 'Selim Ola'})
myDict[1] = 'Adekunle'
# myDict = {}.fromkeys([4,2,3], 3)
myDict.pop(1)
myDict.setdefault(1, 'Default')
myDict.popitem()
myDict.popitem()

# # SET METHODS
set1 = {1,2,3,4,5,10,20,30,40,59}
set2 = {10,20,30,40,59} # 3,5,7,6,8
set1.discard(41)
print(set1)
print(set2.issubset(set1))

users = [
    {'id': 1, 'name': 'Adeola', 'age': 30},
    {'id': 2, 'name': 'Adekola', 'age': 50},
]

info = {'id': 3, 'name': 'Olu', 'age': 18}
users.append(info)

# print(users)

