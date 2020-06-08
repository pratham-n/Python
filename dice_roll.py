import random
import time
max=6
min=1

roll_again='y'

while roll_again=='y' or roll_again=='Y':
    print("Rolling dice....")
    time.sleep(random.randint(1, 4))
    print(random.randint(min, max))
    roll_again=input("Do you want to roll again?(y/n)")
