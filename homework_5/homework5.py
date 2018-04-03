import datetime
import os
from homework_5 import check_functions
os.environ["CARD_TYPE"] = "China"


while True:
    card_number = input("Insert card number in view - XXXX XXXX XXXX XXXX\n")

    if check_functions.proverka_card_num(card_number):
        print("Not valid card number!")
        continue
    if card_number[0] == 5167:
        print("You use PrivatBank credit card")
    elif card_number[0] == 5167:
        print("You use Monobank credit card")
    else:
        print("You use credit card from the unknown bank")
    break
while True:
    mm, yy, cvv= input("Input expire date and CVV\n").split("/")
    if check_functions.proverka_cvv(mm, yy, cvv):
        continue
    else:
        break

print(f"All is OK! Card number - {card_number}, expire date - {mm}/{yy}, CVV - {cvv}")


