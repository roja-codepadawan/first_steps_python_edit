# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# name1 = name1.lower()
# name2 = name2.lower()

bothnames = name1.lower() + name2.lower()
t = bothnames.count("t")
r = bothnames.count("r")
u = bothnames.count("u")
e = bothnames.count("e")
first_digit = t + r + u + e

l = bothnames.count("l")
o = bothnames.count("o")
v = bothnames.count("v")
e = bothnames.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
# print(f"{score}%")

if (score < 10) or (score > 90):
  print(f"Your score is {score}%, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}%, you are alright together.")
else:
  print(f"Yourscore is {score}%")
