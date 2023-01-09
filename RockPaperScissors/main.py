# Rock Paper Scissors
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
 ---'    ____)____
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

print("Hello! Let's play rock, paper, scissors")

choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
else:
    print(scissors)

print ("Computer choose:")
import random
computer_choose=random.randint(0,2)

if computer_choose ==0:
    print(rock)
elif computer_choose ==1:\
    print(paper)
else:
    print(scissors)

if (choose == 0 and computer_choose == 0) or (choose == 1 and computer_choose == 1) or (choose == 2 and computer_choose == 2):
    print ("The draw play")
elif (choose == 0 and computer_choose ==2) or (choose == 1 and computer_choose == 0) or (choose == 2 and computer_choose == 1):\
    print ("You win!!!")
else:
    print("You lost")