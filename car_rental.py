print("Welcome to car rentals!")
response = input("Would you like to continue (y/n)? ")

while response == "y":
    cust_code = input("Customer code (b or d): ")
    nr_days = int(input("Number of days: "))
    od_start = int(input("Odometer reading at the start: "))
    od_end = int(input("Odometer reading at the end: "))
    miles = od_end - od_start
    print("Miles driven:", miles)
    amount = 0
    extra_miles = 0

    if miles > nr_days * 100:
        extra_miles = miles - nr_days * 100 
    if cust_code == "b":
        amount = nr_days * 40 + .25 * miles
    else:
        amount = nr_days * 60 + .25 * extra_miles

    print("Amount due:", round(amount,1))
    response = input("Would you like to continue (y/n)? ")
        


    