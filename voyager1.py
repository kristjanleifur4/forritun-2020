#Prompt user for number of days and convert the string to integer
nr_of_days = input('Number of days after 9/25/09: ')
days = int(nr_of_days)

#Starting distance
mile_start = 16637000000
km_start = mile_start*1.609344
au_start = mile_start/92955887.6

#Calculate distance each day does
mile_day = 38241*24
km_day = mile_day*1.609344
au_day = mile_day/92955887.6

#Print out solution
print('Miles from the sun:', mile_start + mile_day*days)
print('Kilometers from the sun:', round(km_start + km_day*days))
print('AU from the sun:', round(au_start + au_day*days))