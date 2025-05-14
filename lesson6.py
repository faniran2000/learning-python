# FUNCTION IN PYTHON
'''
def functionName (param1, paramn=1):
    function body
    function body
    function body
'''
def sayHi(who):
    print('Hi,', who)

# sayHi('Selim')
# sayHi('Adekola')

# for i in range(5):
#     sayHi('A')

# names = ['Adeola', 'Edris', 'Akinkunmi', 'Fawas']
# for name in names:
#     sayHi(name)

# def addTwoNum(first=9, second=30):
#     print('The addition of', first, '+', second, '=', first + second)

# try:
#     first, second = input('Enter 2 number seperated by comma: ').split(',')
#     addTwoNum(int(first), int(second))
# except:
#     print('Invalid input!')

# addTwoNum()

def square(num: int):
    return num**2

# for i in range(1, 101):
#     print(square(i))

# def Sum(*num):
#     sum = 0
#     for n in num:
#         sum += n
#     print(sum)

# # square(10, 50)
# Sum(10, 50, 70, 20)

# def product(*num):
#     product=1
#     for n in num:
#         product *= n
#     print(product)
# product(10, 20, 30)

# def factorial(num):
#     if num < 2:
#         return 1
#     else:
#         p = 1
#         for i in range(1, num + 1):
#             p *= i
#         return p
# print(factorial(2))

# print() recursive

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

print(fact(20))