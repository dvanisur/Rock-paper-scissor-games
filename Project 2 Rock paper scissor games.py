#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Project:2 (Rock/Paper/scissore) games
import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]
print("Welcome to our world")
while True :
    user_input = input("Please type Rock/Paper/scissore or Q to quit: ").lower()
    print(f"Youse chose : {user_input}")
    if user_input == "q":
        break
        
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    #rock: 0 ,paper=1,scissor=2
    computer_pick = options[random_number]
    print("Computer picked",computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == " rock":
        print("You won!")
        user_wins +=1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins +=1
    else:
        print("you are loss!")
        computer_wins += 1
    
print("you won", user_wins ,"times")
print("The computer won",computer_wins,"times")
print("Thank you for your valuable time, Good bye! ")


# In[ ]:




