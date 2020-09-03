num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: ")) 

print("The maximum is", max_int)    # Do not change this line



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