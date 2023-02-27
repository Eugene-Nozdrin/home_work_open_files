with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        # print(dish)
        # print('---------')
        lin = int(file.readline())
        # print(lin)
        ingredients = []
        for _ in range(int(lin)):
            emp = file.readline().strip()
            ingredient_name, quantity, measure = emp.split(' | ')
            ingredients.append(
                {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            )
            cook_book[dish] = ingredients
        file.readline()
print(cook_book)


def get_shop_list_by_dishes(dishs, person):
    nec_ing = {}

    for dish in dishs:
        if dish in cook_book:
            for a in cook_book[dish]:
                # print(a)
                if a['ingredient_name'] not in nec_ing:
                    nec_ing[a['ingredient_name']] = {'measure': a['measure'], 'quantity': int(a['quantity']) * person}
                    print(nec_ing[a['ingredient_name']])
                else:
                    nec_ing[a['ingredient_name']]['quantity'] += int(a['quantity']) * person
    print(nec_ing)


d = ['Омлет', 'Утка по-пекински', 'Фахитос']
get_shop_list_by_dishes(d, 3)
