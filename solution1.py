mytuple = (1,2,3,4,5)
mytuple = list(mytuple)
mytuple[1] = 20
# print(tuple(mytuple))

# ===================================================

mytuple = (1,2,30,4,50)
mytuple = mytuple[0:2] + (3,) + mytuple[3:]
print(mytuple)

# str1 = 'Selim'
# str2 = 'Ade'
# combine = '4' + '2'
# print(combine)

# print('I Love python programming language\n' * 1000)

mydict = {1: 'Ade', 4: 'Ola', 3: 'Kunle'}

print(mydict)

num = tuple(range(1, 201))
print(num)