# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person 
# and the program outputs the age in terms of years,months,days TODAY.


from datetime import date

# input_date = input("Enter date of birth as YYYY-MM-DD: ").split("-")
# birthday = [int(item) for item in input_date]

# def calc_age(birthday):
#     age_list =[]
#     today = date.today()
#     cur_day = int(today.strftime("%d"))
#     cur_month = int(today.strftime("%m"))
#     cur_year = today.year

#     years = cur_year - birthday[0]
#     month = cur_month - birthday[1]
#     day = cur_day - birthday[2]

#     age_list.insert(0, years)
#     age_list.insert(1, month)
#     age_list.insert(2, day)

#     return age_list
# age = calc_age(birthday)
    
# print(f'You are {age[0]} years {age[1]} months and {age[2]} days')


input_date = input("Enter date of birth as YYYY-MM-DD: ").split("-")
birthday = [int(item) for item in input_date]

def calc_age(birthday):
    age_list =[]
    today = date.today()
    cur_day = int(today.strftime("%d"))
    cur_month = int(today.strftime("%m"))
    cur_year = today.year

    years = cur_year - birthday[0]
    if birthday[1] > cur_month:
         month = (cur_month + 12) - birthday[1]
         years = years - 1
    else:
         month = cur_month -birthday[1]
    if birthday[2] > cur_day:
        day = (cur_day + 30 or 31) - birthday[2]
        month = month - 1
    else:
         day = cur_day - birthday[2]
  
    age_list.insert(0, years)
    age_list.insert(1, month)
    age_list.insert(2, day)

    return age_list
age = calc_age(birthday)
    
print(f'You are {age[0]} years {age[1]} months and {age[2]} days')
















