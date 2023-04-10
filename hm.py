from pprint import pprint
with open('files.txt', 'rt', encoding='utf-8') as file:
    cook_book = dict()
    for line in file:
        dep_name = line.strip()
        count_ingridients = int(file.readline().strip())
        bludo = []
        for _ in range(count_ingridients):
            ingridient_name, quantity, measure = file.readline().strip().split(' | ')
            bludo.append({
                'ingridient_name': ingridient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dep_name] = bludo
    pprint(cook_book, sort_dicts=False)
    