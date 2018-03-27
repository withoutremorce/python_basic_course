name = input("Name - ")
age = input("Age - ")
email = f"{name}{age}@itea.ua"


try:
    name/"sometext"
    surname = "Noob"
except Exception as e:
    surname = "Klichko"
print("\nDeveloping with Python…\n")
if surname == "Noob":
    print ("Ti dopustil oshibku!")
else: print("Molodec!")