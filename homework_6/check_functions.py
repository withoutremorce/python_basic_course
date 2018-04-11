import datetime
import os
import re


def check_card_num(card_number_def):
    region = os.environ.get("CARD_TYPE", "Europe")
    pattern_credit_number = re.match(r'\d{4}\ \d{4}\ \d{4}\ \d{4}$', card_number_def)
    if region == "China":
        pattern_credit_number = re.match(r'\d{4}\ \d{4}\ \d{4}$', card_number_def)
    if pattern_credit_number:
        return True


def check_cvv(credent):
    pattern_credent = re.match(r'[00-12]{2}\/[00-99]{2}\/[000-999]{3}$', credent)
    mm, yy, cvv = credent.split('/')
    inserted_date = datetime.datetime(2000 + int(yy), int(mm), 1, 1, 1, 1, 1)
    if pattern_credent and inserted_date >= datetime.datetime.now():
        return True


def check_name_secondname(name_secondname):
    pattern_name = re.match(r'[aA-zZ]+\ [aA-zZ]+$', name_secondname)
    if pattern_name:
        return True