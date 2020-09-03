num = int(input("Input a number: ")) # Do not change this line

# Fill in the missing code below
if num < 0:
    print("Negative") # Do not change this line
elif num > 0:
    print("Positive") # Do not change this line
else:
    print("Zero") # Do not change this line



rating = int(input("Input elo rating: ")) # Do not change this line
# Fill in the missing code below

if rating >= 2700:
    print("Super grandmaster") # Do not change this line
elif rating >= 2500:    
    print("Grandmaster") # Do not change this line
elif rating >= 2400:
    print("International") # Do not change this line
elif rating < 2400 and rating > 999:
    print("Amateur") # Do not change this line
else:
    print("Invalid") # Do not change this line



num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

# Fill in the missing code below
if num1 <= num2 and num1 <= num3:
    min_int = num1
elif num2 <= num1 and num2 <= num3:
    min_int = num2
else:
    min_int = num3

print("The minimum is: ", min_int) # Do not change this line    



d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line


if d1 >= 1 and d1 <= 6 and d2 >= 1 and d2 <= 6:
    if d1 == d2:
        print('Pair')
    else:
        print(d1+d2)
else:
    print('Invalid input')



age = int(input("Input age: ")) # Do not change this line

ticket_price = 40
if age >= 65:
    ticket_price = 40*.6
elif age < 20 and age >5:
    ticket_price = 40*.8
elif age <= 5:
    ticket_price = 0

print(float(ticket_price))