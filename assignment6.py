# for counter in range(2):
#     scores=int(input("Enter your score ("+ str(counter + 1) +"): "))
# counter+=1

# def grade(num, num1):
#     print("A")
#     grade(scores>75, scores==75)

#     def score(val1, val2):
#         print("B")
#         score(scores>65,scores==65)
#     counter+=1
def get_scores():
    scores = []
    for counter in range(10):
        score = int(input(f"Enter your score ({counter + 1}): "))
        scores.append(score)
    return scores

def determine_grade(score):
    if score >= 75:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"

def print_grades(scores):
    for i, score in enumerate(scores, start=1):
        grade = determine_grade(score)
        print("="*100)
        print(f"Grade for score {score} ({i}): {grade}")

def main():
    scores = get_scores()
    print_grades(scores)

if __name__ == "__main__":
    main()
        
        
