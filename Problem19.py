# https://projecteuler.net/problem=19
# Tried to do this one without importing the date/time library
# Needs two runs, one to determine which number(0 to 6) is associated with a specific day
# After we do another run with the end year at 1901

jan = 31
feb = 28
mar = 31
april = 30
may = 31
june = 30
july = 31
aug = 31
sept = 30
octo = 31
nov = 30
dec = 31

date_list = [dec, nov, octo, sept, aug, july, june, may, april, mar, feb, jan]

year = 2000
end_year = 1900

day_counter = [0,0,0,0,0,0,0]

leap_tracker = 0
day_tracker = 0

# change sunday depending on the first run
sunday = 0 
sunday_tracker = 0

for year in range(year, end_year, -1):
    for month in date_list.copy():
        if (leap_tracker % 4 == 0):
            if year != 1900:
                if month == 28:
                    month = month + 1
        for day in range(1, month +1):
            print(str(day_tracker % 7) + " " + str(year) + " " + str(month) + " " + str(day))
            if day == 1:
                if day_tracker % 7 == 1:
                    sunday_tracker +=1
            day_counter[day_tracker % 7] += 1
            day_tracker += 1
    leap_tracker += 1

print(day_counter)
print(sunday_tracker)