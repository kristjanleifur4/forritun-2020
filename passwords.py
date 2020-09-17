valid = 0
tries = 0

new_pw = input("Enter a new password: ")
tries += 1

# Check if the length is correct as long as user doesn't quit and count the nr. of inputs as tries
while len(new_pw) < 6 and new_pw != "q" or len(new_pw) > 20:
    print("Invalid length")
    new_pw = input("Enter a new password: ")
    tries += 1

# Output if user quits, we don't count quits as a try
if new_pw == "q":
    tries -= 1
    print("You tried {} passwords, {} valid, {} invalid".format(tries, valid, tries - valid))

# while correct length is inputted, check if it contains required number and upper/lower case
while len(new_pw) >= 6 and len(new_pw) <= 20:
    if not any (ch.islower() for ch in new_pw):
        print("At least one lower case letter needed")
    if not any (ch.isupper() for ch in new_pw):
        print("At least one upper case letter needed")
    if not any (ch.isdigit() for ch in new_pw):
        print("At least one number needed")
    # if all requirements are met, print out that the password is valid and count the try as valid
    if any (ch.isupper() for ch in new_pw) and any (ch.islower() for ch in new_pw) and any (ch.isdigit() for ch in new_pw):
        print("Valid password of length {}".format(len(new_pw)))
        valid += 1
    # continue to ask user for input until he decides to quit
    new_pw = input("Enter a new password: ")
    tries += 1
    while len(new_pw) < 6 and new_pw != "q" or len(new_pw) > 20:
        print("Invalid length")
        new_pw = input("Enter a new password: ")
        tries += 1
    if new_pw == "q":
        tries -= 1
        print("You tried {} passwords, {} valid, {} invalid".format(tries, valid, tries - valid))







