import math

def sum_natural(n_str):
    nat_sum = 0
    if n_str.isdigit():
        n_int = int(n_str)
        if n_int >= 2:
            for i in range(0, n_int + 1):
                nat_sum += i
        else:
            return print("Error: {} was not a valid number.".format(n_str))
    else:
        return print("Error: {} was not a valid number.".format(n_str))
    return print("Natural number sum: {}".format(nat_sum))

def sum_fibonacci(n_str):
    fibo_sum = 0
    if n_str.isdigit():
        n_int = int(n_str)
        if n_int >= 2:
            first = 1
            second = 0
            for i in range(0, n_int - 1):
                third = second
                second = first
                fibo_sum += first
                first = second + third 
        else:
            return print("Error: {} was not a valid number.".format(n_str))      
    else:
        return print("Error: {} was not a valid number.".format(n_str))
    return print("Fibonacci sum: {}".format(fibo_sum))

def approximate_euler(n_str):
    euler_sum = 1
    if n_str.isdigit():
        n_int = int(n_str)
        if n_int >= 2:
            for i in range(1, n_int):
                euler_sum += (1/math.factorial(i))
                rounded = round(euler_sum, 5)
        else:
            return print("Error: {} was not a valid number.".format(n_str))
    else:
        return print("Error: {} was not a valid number.".format(n_str))
    return print("Euler approximation: {}".format(rounded))

def display_menu():
    print("Please choose one of the options below:")
    print("a. Display the sum of the first N natural numbers.")
    print("b. Display the sum of the first N Fibonacci numbers.")
    print("c. Display the approximate value of e using N terms.")
    print("x. Exit from the program.")

def main():
    display_menu()
    print()
    menu_choice = input("Enter option: ")
    while menu_choice != "x":
        if menu_choice == "a":
            n_str = input("Enter N: ")
            sum_natural(n_str)
            print()
            menu_choice = input("Enter option: ")
        elif menu_choice == "b":
            n_str = input("Enter N: ")
            sum_fibonacci(n_str)
            print()
            menu_choice = input("Enter option: ")
        elif menu_choice == "c":
            n_str = input("Enter N: ")
            approximate_euler(n_str)
            print()
            menu_choice = input("Enter option: ")
        elif menu_choice != "a" or menu_choice != "b" or menu_choice != "c":
            print("Unrecognized option {}".format(menu_choice))
            display_menu()
            print()
            menu_choice = input("Enter option: ")
    
    
    

main()

