# Практика задача 1
int_numbers = [i for i in range(1, 11)]
for number in int_numbers:
    print(number + 1)

# Практика задача 2
string = input('Введите строку: ')
for letter in string:
    print(letter)

# Оценки
school_journal = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
{'school_class': '4b', 'scores': [5, 3, 2, 4, 3]},
{'school_class': '4c', 'scores': [4, 3, 2, 5, 4]},
{'school_class': '5a', 'scores': [3, 5, 3, 5, 2]},
{'school_class': '5b', 'scores': [2, 4, 5, 5, 3]}]

sum_scores = 0
count_scores = 0

for classes in school_journal:
    sum_scores += sum(classes['scores'])
    count_scores += len(classes['scores'])
    mid_class_score = sum(classes['scores']) / len(classes['scores'])
    print('Средний бал в классе {} равен {}'.format(classes['school_class'], mid_class_score))
print('Средний бал по школе равен {}'.format(sum_scores / count_scores))