#Algorithm
# the sequence takes the last 3 numbers and adds them together to make a new int
# this is then repeated for the same number of steps
n = int(input("Enter the length of the sequence: "))
counter = 1
total = 0
first = 0
second = 0
third = 1


while counter <= n:
    total = first + second + third
    print(total)

    first = second
    second = third
    third = total

    if first == 1 and second == 1:
        first = 0 

    counter += 1 # Do not change this line