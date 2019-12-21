"""
В введённом диапазоне обнаружить числа кратные 3
"""

first_value = float(input("Введите первое число (нижняя граница): "))
second_value = float(input("Введите второе число (верхняя граница): "))
result = []
join_sign = ', '

while int(first_value) < int(second_value):
    if int(first_value) % 3 == 0:
        result.append(str(int(first_value)))

    first_value += 1

print('Целые числа диапазона, кратные 3:', join_sign.join(result))