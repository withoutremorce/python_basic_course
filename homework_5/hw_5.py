import datetime
# current_date = datetime.datetime.now()


def proverka_card_num(card_number_def):
    znachenie = True
    card_number_def = card_number_def.split(" ")
    if len(card_number_def) == 4:
        for i in card_number_def:
            if len(i) == 4:
                 try:
                    i = int(i)
                    znachenie = False
                 except ValueError:
                     return True
            else:
                return True
    else:
        return True
    return znachenie


def proverka_cvv(mm, yy, cvv_znachenie):
    if len(mm) == 2 and len(yy) == 2 and len(cvv_znachenie) == 3:
        try:
            mm = int(mm)
            yy = int(yy)
            int(cvv_znachenie)
            inserted_date = datetime.datetime(2000 + yy, mm, 1, 1, 1, 1, 1)
            if inserted_date <= datetime.datetime.now():
                print("Not valid expire date")
                return True
            else:
                return False
        except ValueError:
            print("Not valid expire date format")
            return True
    else:
        print("Not valid expire date format")
        return True


while True:
    card_number = input("Insert card number in view - XXXX XXXX XXXX XXXX\n")

    if proverka_card_num(card_number):
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
    if proverka_cvv(mm, yy, cvv):
        continue
    else:
        break

print(f"All is OK! Card number - {card_number}, expire date - {mm}/{yy}, CVV - {cvv}")


