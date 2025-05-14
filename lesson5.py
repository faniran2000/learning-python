# Pattern Drawing Using Python

# for r in range(5):
#     for c in range(5):
#         if r == 0 or r == 4 or c == 0 or c == 4:
#             print('@ ', end='')
#         else:
#             print(' ', end=' ')
#     print()

# for r in range(5):
#     for c in range(5):
#         if r == 4 or c == 0 or c == r:
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     print()

# for r in range(5):
#     for c in range(5):
#         if r==0 or c==4 or c==r:
#             print("*", end="")
#         else:
#             print(' ', end="")
#     print()

# for r in range(7):
#     for c in range(7):
#         if r==4 or c==4 or r==2 or c==2 or r==1 or c==1 or r==2 or c==2 or r==4 or c==4 or r==5 or c==5 or r==6 or c==6 or r==7 or c==7 or  c==r:
#             print("*", end="")
#         else:
#             print(' ', end="")
#     print()

# for r in range(5):
#     for c in range(5):
#         if (r in [0,4] and c not in [0, 4]) or (c in [0,4] and r not in [0, 4]):
#             print(f'@ ', end='')
#         else:
#             print('  ', end='')
#     print()

for r in range(5):
    for c in range(11):
        if (c == 0 or c==4 or (r == 2 and c < 5)) or ((r==0 or c==8) and c>5 or (r==0 or c==3 or r==3 or c==2 or c==3) and c>5):
            print(f'@ ', end='')
        else:
            print('  ', end='')
    print()
"""
print('''
@ @ @ @ @ @
@         @
@         @
@         @
@ @ @ @ @ @
''')
"""