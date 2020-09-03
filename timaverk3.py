num = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below

while num >= 1:
    print(num)
    num = num - 1



num = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
counter = 1
evn = 2
while num  >= counter:
    print(evn)
    counter += 1
    evn += 2



num = int(input("Input an int: ")) # You can copy this line but not change it

# Fill in the missing code below
summ = 0
while num != 10:
    summ += num
    num = int(input("Input an int: "))
print(summ)




n = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below

factor = 1

while factor <= n:
    if n % factor == 0:
        print(factor)
    factor += 1




rating = int(input("Input elo rating: ")) # Do not change this line
# Fill in the missing code below

while rating > 1:
    if rating >= 2700:
        print("Super grandmaster") # Do not change this line
    elif rating >= 2500:
        print("Grandmaster") # Do not change this line
    elif rating >= 2400:
        print("International") # Do not change this line
    elif rating < 2400 and rating >= 1000:
        print("Amateur") # Do not change this line
    elif rating < 1000:
        print("Invalid") # Do not change this line
    rating = int(input("Input elo rating: ")) # Do not change this line




a0 = int(input("Input a positive int: "))   # Do not change this line

print(a0)
while a0 != 1:
    if a0 % 2 == 0:
        a0 = a0 // 2
        print(a0)
    else:
        a0 = a0 * 3 + 1
        print(a0)




