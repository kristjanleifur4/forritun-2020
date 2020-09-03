upto = int(input("Input an int: "))  # Do not change this line

for i in range(1,upto):
    print(i)



highest = int(input("Input an int: "))

for i in range(1,highest+1):
    if i % 3 == 0:
        print(i)



first = int(input("Input the first integer: "))
second = int(input("Input the second integer: "))

multiple = 0

for i in range(1,second+1):
    multiple = multiple + first
print(multiple)



max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

# Fill in the missing code
days_when_amount_acquired = 0
summ = 0
dayz = 0

for i in range(0,max_days):
    summ = summ + 2**i
    dayz += 1
    if summ == target:
        days_when_amount_acquired = dayz

print('Days needed:',days_when_amount_acquired)




num = int(input("Input an int: ")) # Do not change this line

summ = 0

for i in range(1, num+1):
    summ += i
    print(summ)


length = int(input("Input the length of series: "))

summ = 0


for i in range(1,length+1):
    if i % 2 == 0:
        summ -= (i*2)
        print(-i*2)
    else:
        summ += (i*2)
        print(i*2)
print("Sum:", summ)
    