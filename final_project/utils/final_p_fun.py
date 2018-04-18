from random import choice
from string import digits
import string
import random


def fill_info(name, second_name):  # name, second_name
    credent = random.choice(name) + " " + random.choice(second_name)   # creating a normal - look human
    phone = list("+380" + ''.join(random.choice(digits) for i in range(9)))   # list of phone number for future upgrade
    # bad_symbols for phone number
    bad_symbols_phone = ("[", "-", "]", " ", str(random.choice(string.ascii_uppercase + string.ascii_lowercase)))
    # bad_symbols for phone number
    bad_symbols_card = ("-", " ", str(random.choice(string.ascii_uppercase + string.ascii_lowercase)))
    if random.randint(1, 50) == 1:
        phone[random.randint(1, len(phone)-1)] = random.choice(bad_symbols_phone) # change a rand element
    phone = ''.join(phone)  # phone to normal look
    mm = str(random.randint(0, 12))  # random month
    yy = str(random.randint(18, 99))  # random year
    if len(mm) == 1:
        mm = "0"+mm   # month to normal look
    exp_date = mm+"/"+yy
    card = list(''.join(choice(digits) for i in range(4)) +   # generating a card
                ''.join(choice(digits) for i in range(4)) +
                ''.join(choice(digits) for i in range(4)) +
                ''.join(choice(digits) for i in range(4)))
    if random.randint(1, 100) == 1:
        card[random.randint(0, len(card)-1)] = random.choice(bad_symbols_card)  # change a rand element
    card = ''.join(card)  # card to string
    card_normal = card[0:4] + ' ' + card[4:8] + ' ' + card[8:12] + ' ' + card[12:16]  # adding spaces to card number
    main_dict = dict({"Name": credent, "Phone": phone, "Exp_day": exp_date, "Card": card_normal})  # gathering a dict
    return main_dict
