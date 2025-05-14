# def accept_scores():
#     scores = []
#     for s in range(10):
#         score = int(input(f'Enter score for student ({s+1}): '))
#         scores.append(score)
#     return scores
# def sumScores(scores):
#     return sum(scores)

# def determine_grade(score):
#     if score >= 75:
#         return "A"
#     elif score >= 70:
#         return "AB"
#     elif score >= 65:
#         return "B"
#     elif score >= 60:
#         return "BC"
#     elif score >= 55:
#         return "C"
#     elif score >= 50:
#         return "CD"
#     elif score >= 45:
#         return "D"
#     elif score >= 40:
#         return "E"
#     else:
#         return "F"
    
# scores = accept_scores()
# total = sumScores(scores)
# grade = determine_grade(total)
# print('_'*100)
# print(f'The summation of entered scores is {total} \nThe grade is {grade}')
# print('\nThe summation of entered scores is {} \nThe grade is {}'.format(total, grade))

for c in range(5):
    for r in range(64):
        if ((r in [0, 3]) or c==2 and r<4) or ((r in [5, 8]) or ((c in [2,0]) and r>4 and r<8) and not (r==8 and c==2))\
            or ((c in [0, 2, 4] and r>9 and r<14) or (c==1 and r==13 or c==3 and r==10))\
                or(((c in [0,4] and r not in [15, 18]) or (r in [15, 18] and c not in [0,4])) and r>14 and r<19)\
                    or ((c in [0, 2, 4] and r>19 and r<24) or (c==1 and r==23 or c==3 and r==20))\
                        or ((c in [0, 2, 4] or r==28) and r>24 and r<29)\
                            or(((c in [0,4] and r not in [30, 33]) or (r in [30, 33] and c not in [0,4])) and r>29 and r<34)\
                                or (r==35)\
                            or(((c in [0,4] and r not in [37, 40]) or (r in [37, 40] and c not in [0,4])) and r>36 and r<41)\
                                or ((c in [0, 2, 4] and r>41 and r<46) or (c==1 and r==45 or c==3 and r==42))\
                                    or ((c in [0, 2, 4] and r>46 and r<51) or r in [47,50])\
                                        or ((c in [0, 2, 4] and r>51 and r<56) or (r == 52 or r==55 and c !=1)):
            print('@ ', end='')
        else:
            print('  ', end='')
    print()