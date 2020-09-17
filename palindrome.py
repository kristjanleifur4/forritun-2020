# palindrome function definition goes here
def palindrome(in_str):
    in_str = in_str.replace(".","").replace("'","").replace(" ","").lower()
    if in_str == in_str[::-1]:
        return True
    return False

input_str = input("Enter a string: ")

# call the function and print out the appropriate message

if palindrome(input_str):
    print("{} is a palindrome.".format(input_str))
else:
    print("{} is not a palindrome.".format(input_str))
