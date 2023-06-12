# Задача №34
vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
poem = input('Введите стих: ').split(' ')
count = 0
count_vowels = []
for word in poem:
    for i in word:
        if i in vowels:
            count += 1
    count_vowels.append(count)
    count = 0
if count_vowels.count(count_vowels[0]) == len(count_vowels):
    print('Парам пам-пам')
else:
    print('Пам парам')

# Задача №36
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end=' ')
        print()


print_operation_table(lambda x, y: x * y)
