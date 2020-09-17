#Your function definition goes here
def valid_date(date_str):
    if len(date_str) == 8:
        if not any (ch == "." for ch in date_str):
            return False
        if not any (ch.isdigit() for ch in date_str):
            return False
        date_str.split(".")
        day = int(date_str[:2])
        month = int(date_str[3:5])
        year = int(date_str[-2:])

        if month.isdigit() == False:
            return False
        if day.isdigit() == False:
            return False
        if year.isdigit() == False:
            return False


        if day > 0 and day <= 31 and month >= 1 and month <= 12 and year >= 0 and year <= 99:
            return True
    return False

date_str = input("Enter a date: ")

if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")  