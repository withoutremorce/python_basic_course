import datetime
import os
from homework_6 import check_functions
os.environ["CARD_TYPE"] = "China"


while True:
    card_number = input("Insert card number in view - XXXX XXXX XXXX XXXX\n")
    if check_functions.check_card_num(card_number):
        if card_number.startswith('1234'):
            print("You use PrivatBank credit card")
        elif card_number.startswith('5167'):
            print("You use Monobank credit card")
        else:
            print("You use credit card from the unknown bank")
        break
    print("Not valid card number!")
while True:
    credentials = input("Input expire date and CVV\n")
    if check_functions.check_cvv(credentials):
        break
    print("Not valid expire date")
while True:
    name_secondname = input("Input name and second name\n")
    if check_functions.check_name_secondname(name_secondname):
        name_secondname = name_secondname.upper()
        break
    print("Not valid Name and Second name!")

print(f"All is OK! Card number - {card_number}, credentials - {credentials}, name and Second Name - {name_secondname}")


