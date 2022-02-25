print('''
           .--.                  Try not.
 ::\`--._,'.::.`._.--'/::     Do or do not.
 ::::.  ` __::__ '  .::::    There is no try.
 ::::::-:.`'..`'.:-::::::
 ::::::::\ `--' /::::::::              -Yoda
''')
print("Welcome to Treasure Island.")
print("May the force be with you.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

reply = input("\nIntroduction\nIn this game you can answer with 'Y' for Yes, 'N for No,'L' for Left or 'R' for Right and '1','2','3' for 1,2 or 3.\nAre you ready to explore the power within you?\n: ").lower()
if reply == "y":
  reply = input("\nWhich side of the force do you want to join?\nThe dark path of power is on the left side.\nYou will find the light side on your right\n: ").lower()
  if reply == "r":
    reply = input("\nYou still have a lot to learn\nWhat skill do you want to learn first?\n1 = Lightsaber\n2 = About the Jedi\n3 = Deathstar\n: ").lower()
    if reply == "1":
      print("It's still too early for that. The risk of getting injured is great.\nGame Over.")
    elif reply == "2":
      print("You found the Force!\nYou Win!")
    elif reply == "3":
      print("That's not a moon, that's a space station.\nGame Over.")
    else:
      print("You chose a door that doesn't exist.\nGame Over.")
  else:
    print("I am not your father.\nGame Over.")
else:
  print("You fell into a hole.\nGame Over.")