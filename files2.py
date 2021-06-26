import pprint

cook_book = {}

with open ("recipes.txt", "r", encoding="utf-8") as file:
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

cooking_list = {}
def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        if dish in cook_book.keys():
            for items in cook_book[dish]:
                amount = {}
                cooking_list[items['ingredient_name']] = amount
                amount['measure'] = items['measure']
                amount['quantity'] = int(items['quantity'])*person_count


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint.pprint(cooking_list)