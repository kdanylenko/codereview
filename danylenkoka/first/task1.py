"""
Здесь нужно определить количество пустых листов
"""

my_list = [[], 2, 3, "Я бешбермак",[],[]]

lists_number = 0

for element in my_list:
    if element == []:
        lists_number += 1

print("Количество пустых листов:",str(lists_number))
