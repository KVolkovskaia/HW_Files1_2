from pprint import pprint

cook_book = {}


with open('recipes.txt', encoding='utf-8') as file:
    for line in file:
        recipes = line.strip()
        ingridients = int(file.readline(2))
        recipe_list = []
        for i in range(ingridients):
            ingredient_name, quantity, measure = file.readline().strip().split(" | ")
            recipe_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
        cook_book[recipes] = recipe_list
        file.readline()

pprint(cook_book, sort_dicts=False, width=150)