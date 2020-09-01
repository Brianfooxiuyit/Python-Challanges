import random
number = 0
total = 0
minimum = 100
maximum = 0
numlist = []
for count in range(50):
    number = random.randint(1,101)
    total = total + number
    if number > maximum:
        number = maximum
    if number < minimum:
        number = minimum
    numlist.append(number)

mean = total / 50
print(total)
print(minimum)
print(maximum)