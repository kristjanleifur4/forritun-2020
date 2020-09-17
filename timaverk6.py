a_str = input("Input a string: ")

print(a_str[0], " ", a_str[-1])


a_str = input("Input a string: ")
# your code here
new_str = a_str[-2:] + a_str[0:-2]
print(new_str)


a_str = input("Input a string: ")
upper = 0
lower = 0

for ch in a_str:
    if (ch.islower()):
        lower += 1
    elif (ch.isupper()):
        upper += 1
print(lower)
print(upper)
    

a_str = input("Input a float: ")
a_float = float(a_str)

print("{:12.2f}".format(a_float))



a_str = input("Input a string: ")
words = 1
letters = 0

for ch in a_str:
    if ch == " ":
        words += 1
    if ch.isalpha() or ch.isdigit():
        letters += 1


print("No. of letters: {}, no. of words: {}".format(letters, words))



name = input("Input a name: ")

names = name.split(", ")
first_name = names[0]
last_name = names[1]

#print(last_name[0].capitalize(),", ",first_name.capitalize())

print("{}. {}".format(last_name[0].capitalize(), first_name.capitalize()))


my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
bin_str = ""
my_input = my_int

while my_int > 0:
    if my_int % 2 == 0:
        bin_str += "0"
    elif my_int % 2 == 1:
        bin_str += "1"
    my_int = my_int // 2

if bin_str == "":
    bin_str += "0"
bin_str = bin_str[::-1]
        
print("The binary of {} is {}".format(my_input,bin_str))
