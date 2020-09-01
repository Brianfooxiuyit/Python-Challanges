isbn = []
num_ar = [2,3,4,5,6,7,8,9,10]
multiplied = 0
multiplied_total = 0
remainder = 0
checkdigit = 0
finaldigit = 0

print("Please input the first number of the code starting from the right hand side (apart from the last number).")
finaldigit = int(input("Please input the next digit: "))
for count in range(9):
    number = int(input("Please input the next digit: "))
    isbn.append(number)
    multiplied = isbn[count] * num_ar[count]
    multiplied_total = multiplied_total + multiplied
remainder = multiplied_total%11
checkdigit = 11 - remainder
if checkdigit == finaldigit:
    print("the isbn code is valid")