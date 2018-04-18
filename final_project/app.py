from final_project.utils import *
import csv

name = ("Vasia", "Jenya", "Natasha", "Tamara", "Bogdan", "Oleh")
second_name = ("Klichko", "Poroshenko", "Fedorenko", "Bolischuk", "Marlin", "Pupkin")
generated_input = []

for i in range(100):
    generated_input.append(fill_info(name, second_name))

# creating a file without errors
with open('cardholders.csv', 'w', newline='') as cardholders_csv:
    header = ["Name", "Phone", "Exp_day", "Card"]
    writer = csv.DictWriter(cardholders_csv, fieldnames=header)
    writer.writeheader()
    for i in range(len(generated_input)):
        if not check_input(generated_input[i]):
            writer.writerow({"Name": generated_input[i].get("Name"), "Phone": generated_input[i].get("Phone"),
                             "Exp_day": generated_input[i].get("Exp_day"), "Card": generated_input[i].get("Card")})

# creating a file for errors
with open('cardholders_erros.csv', 'w', newline='') as cardholders_err:
    header = ["Name", "Phone", "Exp_day", "Card"]
    writer = csv.DictWriter(cardholders_err, fieldnames=header)
    writer.writeheader()
    for i in range(len(generated_input)):
        if check_input(generated_input[i]):
            writer.writerow({"Name": generated_input[i].get("Name"), "Phone": generated_input[i].get("Phone"),
                             "Exp_day": generated_input[i].get("Exp_day"), "Card": generated_input[i].get("Card")})
