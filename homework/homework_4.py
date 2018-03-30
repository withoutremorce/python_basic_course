import datetime
current_date = datetime.datetime.now()

def proverka(card_number_def):
    for i in card_number_def:
        if len(i) == 4:
             try:
                i = int(i)
             except ValueError:
                return True
        else:
            return True
    return False

while True:
    card_number = input("Insert card number in view - XXXX XXXX XXXX XXXX\n")
    card_number = card_number.split(" ")
    if len(card_number) != 4 or proverka(card_number):
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
    mm, yy = input("Input expire date\n").split("/")
    if len(mm) == 2 and len(yy) == 2:
        try:
            mm = int(mm)
            yy = int(yy)
            inserted_date = datetime.datetime(2000 + yy, mm, 1, 1, 1, 1, 1)
            if inserted_date <= current_date:
                print("Not valid expire date")
                continue
            else:
                break
        except ValueError:
            print("Not valid expire date format")
            continue
    else:
        print("Not valid expire date format")
        continue
while True:
    cvv = input("Insert CVV\n")
    if len(cvv) == 3:
        try:
            int(cvv)
        except ValueError:
            print("Error CVV")
            continue
    else:
        continue
    break
print(f"All is OK! Card number - {card_number}, expire date - {inserted_date.month}/{inserted_date.year}, CVV - {cvv}")


