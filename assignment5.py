# for r in range(5):
#     for c in range(11):
#             if r==2 or c==0 and c==4 or c==6:
#                 print("@", end="")
#     print()

def generate_matric_numbers(prefix, year, start_index, end_index):
    for i in range(start_index, end_index + 1):
        matric_number = f"{prefix}{year}{str(i).zfill(5)}"
        print(matric_number)

# Example usage:
prefix = "HR"
year = "2023"
start_index = 102085
end_index = 102095

generate_matric_numbers(prefix, year, start_index, end_index)