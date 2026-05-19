import re

class CustomList:
    def __init__(self, items=None):
        self.data = []

        if items is not None:
            for item in items:
                if not isinstance(item, int):
                    raise TypeError("Список може містити лише цілі числа")
                self.data.append(item)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("Можна присвоювати лише цілі числа")
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    def __iadd__(self, other):
        if isinstance(other, int):
            self.data.append(other)

        elif isinstance(other, CustomList):
            self.data.extend(other.data)

        else:
            raise TypeError("Правий операнд має бути числом або CustomList")

        return self

    def __isub__(self, other):
        if isinstance(other, int):
            values_to_remove = [other]

        elif isinstance(other, CustomList):
            values_to_remove = other.data

        else:
            raise TypeError("Правий операнд має бути числом або CustomList")

        self.data = [x for x in self.data if x not in values_to_remove]

        return self

    # *=
    def __imul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Правий операнд має бути цілим числом")

        self.data *= other
        return self

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

text = input("Введіть текст:\n")

numbers = re.findall(r'-?\d+', text)

numbers = [int(num) for num in numbers]

num_list = CustomList(numbers)

print("\nЗнайдені числа:")
print(num_list)

total_sum = sum(num_list.data)

count_numbers = len(num_list)

print("\nСума чисел:", total_sum)
print("Кількість чисел:", count_numbers)

check_numbers = {1, 3, 1984, 7777}

found = False
for number in check_numbers:
    if number in num_list:
        found = True
        break
import re


class CustomList:
    def __init__(self, items=None):
        self.data = []

        if items is not None:
            for item in items:
                if not isinstance(item, int):
                    raise TypeError("Список може містити лише цілі числа")
                self.data.append(item)

    # Отримання елемента за індексом
    def __getitem__(self, index):
        return self.data[index]

    # Зміна елемента за індексом
    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("Можна присвоювати лише цілі числа")
        self.data[index] = value

    # len()
    def __len__(self):
        return len(self.data)

    # оператор in
    def __contains__(self, item):
        return item in self.data

    # +=
    def __iadd__(self, other):
        if isinstance(other, int):
            self.data.append(other)

        elif isinstance(other, CustomList):
            self.data.extend(other.data)

        else:
            raise TypeError("Правий операнд має бути числом або CustomList")

        return self

    # -=
    def __isub__(self, other):
        if isinstance(other, int):
            values_to_remove = [other]

        elif isinstance(other, CustomList):
            values_to_remove = other.data

        else:
            raise TypeError("Правий операнд має бути числом або CustomList")

        self.data = [x for x in self.data if x not in values_to_remove]

        return self

    # *=
    def __imul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Правий операнд має бути цілим числом")

        self.data *= other
        return self

    # Виведення списку
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


# ==============================
# Робота з текстом
# ==============================

text = input("Введіть текст:\n")

# Пошук усіх цілих чисел
numbers = re.findall(r'-?\d+', text)

# Перетворення у список цілих чисел
numbers = [int(num) for num in numbers]

# Створення CustomList
num_list = CustomList(numbers)

print("\nЗнайдені числа:")
print(num_list)

# Сума чисел
total_sum = sum(num_list.data)

# Кількість чисел
count_numbers = len(num_list)

print("\nСума чисел:", total_sum)
print("Кількість чисел:", count_numbers)

# Перевірка наявності хоча б одного числа
check_numbers = {1, 3, 1984, 7777}

found = False
for number in check_numbers:
    if number in num_list:
        found = True
        break

if found:
    print("У тексті трапляється хоча б одне з чисел {1, 3, 1984, 7777}")
else:
    print("Жодне з чисел {1, 3, 1984, 7777} не трапляється")

# Кількість ненульових чисел (з урахуванням повторів)
non_zero_count = 0

for number in num_list.data:
    if number != 0:
        non_zero_count += 1

print("Кількість ненульових чисел:", non_zero_count)


# ==============================
# Приклади роботи операторів
# ==============================

a = CustomList([1, 2, 3])
b = CustomList([3, 4])

print("\nПочаткові списки:")
print("a =", a)
print("b =", b)

a += b
print("\na += b ->", a)

a += 10
print("a += 10 ->", a)

a -= 3
print("a -= 3 ->", a)

a *= 2
print("a *= 2 ->", a)
if found:
    print("У тексті трапляється хоча б одне з чисел {1, 3, 1984, 7777}")
else:
    print("Жодне з чисел {1, 3, 1984, 7777} не трапляється")

non_zero_count = 0

for number in num_list.data:
    if number != 0:
        non_zero_count += 1

print("Кількість ненульових чисел:", non_zero_count)

a = CustomList([1, 2, 3])
b = CustomList([3, 4])

print("\nПочаткові списки:")
print("a =", a)
print("b =", b)

a += b
print("\na += b ->", a)

a += 10
print("a += 10 ->", a)

a -= 3
print("a -= 3 ->", a)

a *= 2
print("a *= 2 ->", a)