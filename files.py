import pprint
cook_book = {}

file = open("recipes.txt", "r", encoding="utf-8")
for line in file:
    name = line.strip()
    number = int(file.readline().strip())
    comp = []
    for item in range(number):
        ingredients = {}
        ing = file.readline().split("|")
        ingredients["ingredient_name"] = ing[0]
        ingredients["quantity"] = ing[1]
        ingredients["measure"] = ing[2].strip()
        comp.append(ingredients)
    f = file.readline().strip()
    cook_book[name] = comp

pprint.pprint(cook_book)
# print(cook_book)
