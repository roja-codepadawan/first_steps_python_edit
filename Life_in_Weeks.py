# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
# https://waitbutwhy.com/2014/05/life-weeks.html
# Write your code below this line 👇

days = 365
weeks = 52
months = 12

def calculate():
    remaining_years = 90 - int(age)
    remaning_days = remaining_years * days
    reamaning_weeks = remaining_years * weeks
    reamaning_months = remaining_years * months
    print(f"You have {remaning_days} days, {reamaning_weeks} weeks, and {reamaning_months} months left.")

calculate()


"""
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
"""
