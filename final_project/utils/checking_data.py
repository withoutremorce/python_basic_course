import re


def check_input(inserted_dict):
    pattern_for_phone = re.search(r'[a-zA-Z\[\]\-\ ]', inserted_dict.get('Phone'))
    pattern_for_card = re.search(r'[a-zA-Z\-\ ]', (inserted_dict.get('Card')[0:4]+  # shitty variant of checking
                                                   inserted_dict.get('Card')[5:9]+  # without spaces
                                                   inserted_dict.get('Card')[10:14]+
                                                   inserted_dict.get('Card')[15:19]))

    if pattern_for_phone or pattern_for_card:
        return True
    else:
        return False
