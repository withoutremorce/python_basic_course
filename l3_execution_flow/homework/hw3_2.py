import datetime
try:
    nomer = input("Input # of your credit card - ")
    if len(nomer)==16:
        nomer=int(nomer)
    else:
        exit()
except ValueError:
    print("Put in number format!")
    exit()
try:
    mm, yy = input("Paste date of card (mm/yy) - ").split('/')
    d = datetime.date(2000+int(yy), int(mm), 1)
except Exception as e:
    print("OK")
cvv = input("Input cvv - ")
if len(cvv) < 3:
    print("ERROR CVV must be not less than 3 character")
elif ((len(str(nomer))==16) and (type(d) == datetime.date) and (len(cvv) >= 3)) :
    print("Ha- ha- ha. Now I will use your credit card!")