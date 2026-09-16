from datetime import datetime
current_year = datetime.now().year
final_year = int(input("Enter your final year : "))
print("Leap years are : ")
for year in range(current_year, final_year + 1):
    if year % 4 == 0 or (year % 100 == 0 and year % 400 != 0):
        print(year)