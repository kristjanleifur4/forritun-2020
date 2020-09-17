# The function definition goes here
def output_string(input_str):
    for i in input_str:
        return input_str[::2]
        

input_str = input("Enter a string: ")

# You call the function here
print("Every other character:",output_string(input_str))


# Your function definition goes here
def digit_count(input_str):
    digit_count = 0
    for ch in input_str:
        if ch.isdigit():
            digit_count += 1
    return digit_count

input_str = input("Enter a string: ")

# Call the function here

digit_count = digit_count(input_str)

print("No. of digits:", digit_count)


# max_of_three function definition goes here
def find_max(first, second, third):
    maximum = 0
    if first > second and first > second:
        maximum = first
    elif second > first and second > third:
        maximum = second
    else:
        maximum = third
    return maximum
    
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

# Call the function here
maximum = find_max(first, second, third)
print("Maximum:", maximum)


# is_prime function definition goes here
def is_prime(x):
    if x >= 2:
        for i in range(2,x):
            if not ( x % i ):
                return False
    return True

max_num = int(input("Input an integer greater than 1: "))
	        
# Call the function here repeatadly from 2 to max_num and print out the appropriate message
for i in range(2, max_num + 1):
    if is_prime(i):
        print(i,"is a prime")
    else:
        print(i, "is not a prime")


# palindrome function definition goes here
def palindrome(in_str):
    in_str = in_str.replace(".","").replace("'","").replace(" ","").replace(",","").replace("!","").lower()
    if in_str == in_str[::-1]:
        return True
    return False

input_str = input("Enter a string: ")

# call the function and print out the appropriate message

if palindrome(input_str):
    print('"{}" is a palindrome.'.format(input_str))
else:
    print('"{}" is not a palindrome.'.format(input_str))


#Your function definition goes here
def valid_date(date_str):
    if len(date_str) == 8:
        for ch in date_str:
            if ch == "/":
                return False
            if ch.isalpha():
                return False
        date_str.split(".")
        day = int(date_str[:2])
        month = int(date_str[3:5])
        year = int(date_str[-2:])
        if day > 0 and day <= 31 and month >= 1 and month <= 12 and year >= 0 and year <= 99:
            return True
    return False

date_str = input("Enter a date: ")

if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid") 