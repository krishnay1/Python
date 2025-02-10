#Project1
#Rock ,Paper & Scissors Game
########################################

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


a=[rock,paper,scissors]
b=int(input("Enter ur choice? 0 for rock , 1 for paper, 2 for scissor :"))
if b==0:
    print(a[0])
elif b==1:
    print(a[1])
elif b==2:
    print(a[2])
else:
    print("Wrong input")

c=a[random.randint(0,2)]
print("computer choose:")
print(c)

if (b==0 and c==a[0]) and (b==1 and c==a[1]) and (b==2 and c==a[2]):
    print("Game drawn")
elif (b==0 and c==a[1]) or (b==1 and c==a[2]) or (b==2 and c==a[0]):
    print("You Lose")
elif (b==0 and c==a[2]) or (b==1 and c==a[0]) or (b==2 and c==a[1]):
    print("You win")





