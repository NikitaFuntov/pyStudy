full_name = input("Введіть своє ПІБ: ")
first_name, last_name, middle_name = full_name.split()

name_length = len(first_name)
last_name_length = len(last_name)
middle_name_length = len(middle_name)
total_length = name_length + last_name_length + middle_name_length

print(f"Ім'я: {first_name} ({name_length})")
print(f"Прізвище: {last_name} ({last_name_length})")
print(f"По-батькові: {middle_name} ({middle_name_length})")
print(f"Загальна довжина: {total_length}")

print()

elements = [1, "text", 3.14, True]

for element in elements:
    print(f"ID: {id(element)}, Тип: {type(element)}")

print()

bio = """
Мене звуть Микита. Я студент мобильного звязку.
Моя основна мета - просто навчитичя программувати.
"""

print(bio)





