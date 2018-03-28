name = input("Input name - ")
city = input("Input city - ")

try:
    age = int(input("Input your age - "))
except ValueError:
    print("Put age in number format!")

try:
    print(f"Ti rodilsya v {2018-age} gody")
except NameError:
    print("Ne vveden vozrast")

if city == "Kiev":
    print("Kiev is a capital of Ukraine.")
elif city == "Moscow":
    print("Moscow is capital of Russia.")
elif not "Washington" or city == "Poltava":
    print("Better move to Kiev.")
else:
    print ("You are live in very rare city!")