new_pw = input("Enter a new password: ")

upper = 0
lower = 0
digit = 0
valid = 0
invalid = 0

while len(new_pw) < 6 and new_pw != "q" or len(new_pw) > 20:
    invalid += 1
    print("Invalid length")
    new_pw = input("Enter a new password: ")

if new_pw == "q":
    print("You tried {} passwords, {} valid, {} invalid".format(valid + invalid, valid, invalid))



while len(new_pw) >= 6 and len(new_pw) <= 20:
    for ch in new_pw:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1    
    if upper > 0 and lower > 0 and digit > 0:
        print("Valid password of length {}".format(len(new_pw)))
        valid += 1
        upper = 0   
        lower = 0
        digit = 0
    elif upper == 0 and digit == 0:
        invalid += 1
        print("At least one upper case letter needed")
        print("At least one number needed")
    elif lower == 0 and digit == 0:
        invalid += 1
        print("At least one lower case letter needed")
        print("At least one number needed")
    elif upper == 0 and lower == 0:
        invalid += 1
        print("At least one lower case letter needed")
        print("At least one upper case letter needed")
    elif digit == 0:
        invalid += 1
        print("At least one number needed")
    elif upper == 0:
        invalid += 1
        print("At least one upper case letter needed")
    elif lower == 0:
        invalid += 1
        print("At least one lower case letter needed")
    upper = 0   
    lower = 0
    digit = 0
    new_pw = input("Enter a new password: ")
    while len(new_pw) < 6 and new_pw != "q" or len(new_pw) > 20:
        invalid += 1
        print("Invalid length")
        new_pw = input("Enter a new password: ")
    if new_pw == "q":
        print("You tried {} passwords, {} valid, {} invalid".format(valid + invalid, valid, invalid))

    







