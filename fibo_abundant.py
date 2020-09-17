choice = input("Input f|a|b (fibonacci, abundant or both): ")

if choice == "f":
    length = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")
    first = 1
    second = 0
    print(second)
    for i in range(0, length - 1):
        print(first)
        third = second
        second = first
        first = second + third

elif choice == "a":
    max_nr = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    summ = 0
    for i in range(1, max_nr + 1):
        for j in range(1, i):
            if i % j == 0:
                summ = summ + j
        if summ > i:
            print(i)
        summ = 0

elif choice == "b":
    length = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")
    first = 1
    second = 0
    print(second)
    for i in range(0, length - 1):
        print(first)
        third = second
        second = first
        first = second + third

    max_nr = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    summ = 0
    for i in range(1, max_nr + 1):
        for j in range(1, i):
            if i % j == 0:
                summ = summ + j
        if summ > i:
            print(i)
        summ = 0

        