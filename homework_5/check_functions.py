import datetime
import os


def proverka_card_num(card_number_def):
    znachenie = True
    region = os.environ.get("CARD_TYPE", "Europe")
    print(region)
    code_lenth = 4
    if region == "China":
        code_lenth = 3
    card_number_def = card_number_def.split(" ")
    if len(card_number_def) == code_lenth:
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