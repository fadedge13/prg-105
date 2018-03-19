import random


class Dice:
    def __init__(self):
        self.my_roll = 1

    def roll(self):
        self.my_roll = random.randint(1,7)

    def get_my_roll(self):
        return self.my_roll

def main():
    my_dice= Dice()
    my_dice_two = Dice()
    my_dice.roll()
    my_dice_two.roll()
    die_1 = my_dice.get_my_roll()
    die_2 = my_dice_two.get_my_roll()
    print('This roll is', die_1)
    print('This roll is', die_2)
    print('The total is', die_1 + die_2)
    total = die_1 + die_2
    if total == 7 or total == 11:
        print('You win!')
    else:
        print('You lose.')



main()
