'''
Rock = 1
Paper = 0
Scissors = -1
'''
import random
computer = random.choice([1,-1,0])
userstr = input("Enter your choice:")

userdict = {"r" : 1, "p" : 0, "s" : -1}
reversedict= { 1 : "rock", 0 : "paper", -1 : "scissors"}

user = userdict[userstr]

print(f" user chose {reversedict[user]}\n computer chose {reversedict[computer]}")

if(computer == user):
     print("it's a draw 🤝")
else:
   if(computer == 1 and user == 0):
     print("you win 👏🏻")
   elif(computer == 0 and user == 1):
     print("you lose 😢")
   elif(computer == -1 and user == 0):
     print("you win 👏🏻")
   elif(computer == 0 and user == -1):
     print("you lose 😢")
   elif(computer == -1 and user == 1):
     print("you win 👏🏻")
   elif(computer == 1 and user == -1):
     print("you lose 😢")
   else:
     print("Something went wrong")
