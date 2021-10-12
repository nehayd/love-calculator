# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1.lower() + name2.lower()
true = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love = names.count("l") + names.count("o") + names.count("v") + names.count("e")

score = true*10 + love

if score < 10:
  print("Your score is %s, you go together like coke and mentos."%score)
elif 40 < score <50:
  print("Your score is %s, you are alright together."%score)
else:
  print("Your score is %s."%score)