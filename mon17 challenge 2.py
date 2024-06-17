fruit_list = ["Apple", "Orange", "Pineapple", "Banana", "Strawberries"]
print(fruit_list[1])
print(fruit_list[0:3])

fruit_dict = {"Apple": 0.50, "Orange": 0.39, "Pineapple": 1.00, "Banana": 0.29, "Strawberries": 1.50}
prifruit_dict = {"Apple": 0.50, "Orange": 0.39, "Pineapple": 1.00, "Banana": 0.29, "Strawberries": 1.50}

print("Price of Pineapple: £{:.2f}".format(fruit_dict["Pineapple"]))

for fruit, price in fruit_dict.items():
    print(fruit, "%.2f" % price)

fruit_dict = {"Apple": 0.50, "Orange": 0.39, "Pineapple": 1.00, "Banana": 0.29, "Strawberries": 1.50}

fruit_dict["Apple"] = 0.55

print(fruit_dict["Apple"])

fruit_dict = {"Apple": 0.50, "Orange": 0.39, "Pineapple": 1.00, "Banana": 0.29, "Strawberries": 1.50}

fruit_dict = {"Apple": 0.50, "Orange": 0.39, "Pineapple": 1.00, "Banana": 0.29, "Strawberries": 1.50}


for fruit in fruit_dict:
    fruit_dict[fruit] = round(fruit_dict[fruit] * 1.12, 2)

print(fruit_dict)