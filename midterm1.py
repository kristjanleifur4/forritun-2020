number_to_multiply = int(input("Input number to multiply: ")) # Do not change this line
how_often = int(input("Input how often to multiply: ")) # Do not change this line


for i in range(number_to_multiply, (how_often * number_to_multiply) + 1, number_to_multiply):
    print(i)



#fyrsta ár er 15, annað 9 og öll hin samsvara 4 hvert

dog_age = int(input("Input dog's age: ")) # Do not change this line
human_age = 0

if dog_age <= 0 or dog_age > 16:
    print("Invalid age")

while dog_age > 0 and dog_age <= 16:
    if dog_age == 1:
        human_age = 15
    elif dog_age == 2:
        human_age = 24
    elif dog_age > 2:
        human_age = 28 + 4*(dog_age - 3)
    print("Human age:", human_age)
    break



import math

start_int = int(input("Input starting integer: "))


while start_int >= 2:
    result = round(math.sqrt(start_int), 4)
    start_int = result
    print(result)
    

max_int = int(input("Input max integer: "))

for i in range(0, max_int + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


