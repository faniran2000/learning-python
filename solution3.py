# scores = []
# for s in range(1, 15):
#     score = float(input("Enter score for Student (" + str(s)+"): "))
#     scores.append(score)
# print("="*100)
# print("Bellow are the Students Scores:", scores, sep='\n')

# cnt = 2
# while cnt <= 100:
#     is_prime, cnt2 = 0, 1
#     while cnt2 <= cnt:
#         if cnt % cnt2 == 0:
#             is_prime += 1
#         cnt2 += 1
#     if is_prime == 2:
#         print(cnt)
#     cnt += 1
message = [ ]
for msg in range(14):
    try:
        message1=int(input("Enter message ("+ str(msg + 1) +"): "))
        message.append(message1)
    except:
        print("invalid Input, Please Try Again!") 
        message1=int(input("Enter message ("+ str(msg + 1) +"): "))
        message.append(message1)
print(message)
