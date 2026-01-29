#dice rolling problem
import random
if True:
 choice = input('roll the dice(y/n)').lower()

 if choice == 'y':
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f'({die1},{die2})')
    if (die1 > die2):
        print("ok so die1 is greater than die2")
    else:
        print ("ok so die2 is greater than die 1")

 elif choice == 'n':
  print("thanks for displaying ")
 else:
   print("sorry you cannot say that")
