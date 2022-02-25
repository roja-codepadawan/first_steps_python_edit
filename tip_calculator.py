#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
""""
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")
"""

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip_in_percent = input("Howe much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_per_person = float(bill) / int(people)
bill_per_person = float(bill_per_person)
tip = 1 + int(tip_in_percent) / 100
tip_in_dollar = float(bill_per_person) * float(tip) - float(bill_per_person)
tip_in_dollar = round(tip_in_dollar, 2)
person_pay = float(bill_per_person) + float(tip_in_dollar)
person_pay = round(person_pay, 2)

print(
    f"Totale Bill = {bill}$ \nBill per person = {bill_per_person}$ \nTip is {tip_in_percent}% = {tip_in_dollar}$ \n{people} People split the Bill \nEach person should pay = {person_pay}$"
)
