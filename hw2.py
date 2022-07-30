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

# pprint(cook_book, sort_dicts=False, width=150)

# get_shop_list_by_dishes(['Запеченный картофель'])

def get_shop_list_by_dishes(dishes, person):
    dishes_dict = {}
    for i in dishes:
        if i not in cook_book.keys():
            print('Рецепт не найден')
            return
        else:
            ingredients_list = cook_book[i]
            for i in ingredients_list:
                y = i.setdefault('ingredient_name')
                z = {'measure': i.setdefault('measure'), 'quantity': int(i.setdefault('quantity')) * person}
                if y not in dishes_dict.keys():
                    dishes_dict[y] = z
                else:
                    dishes_dict[y] = {'measure': i.setdefault('measure'),
                                      'quantity': i.setdefault('quantity') + str(dishes_dict[y]['quantity'])}
    pprint(dishes_dict, sort_dicts=False)
    return


get_shop_list_by_dishes(['Омлет','Фахитос'], 4)