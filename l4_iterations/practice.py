x=1
y=100
my_list=[]
while True:
    chislo = input("What is your favorite number from 1 to 100?\n")
    try:
        chislo = int(chislo)
        my_list.append(chislo)
        if chislo < x:
            print(f"Your input value {chislo} is less than 1\n")
            continue
        elif chislo > y:
            print(f"Your input value {chislo} is more than 100\n")
            continue
        else:
            my_list.append(chislo)
            break
    except ValueError:
        my_list.append(chislo)
        continue
new_list = [i for i in my_list if type(i) == str]
print(my_list)
print(new_list)