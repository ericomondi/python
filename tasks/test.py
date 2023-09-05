import calendar
from datetime import date

def sub_mnth():
    today = date.today()
    month = int(today.strftime("%m"))



# month = 2   # February
# year = 2023
 
# num_days = calendar.monthrange(year, month)[1]
 
# print("Number of days is",num_days) 

print(month)