# Практика: Возраст
age = abs(int(input('Введите ваш возраст: ')))
def activity(age):
    if age < 7:
        return 'Вы должны учиться в детском саду'
    elif age in range(8, 18):
        return 'Вы должны учиться в школе'
    elif age in range(19, 25):
        return 'Вы студент'
    else:
        return 'Вы работаете'

age = activity(age)
print(age)

# Практика: Сравнение строк
def two_strings(str1, str2):
    if type(str1) != str or type(str2) != str:
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn':
        return 3
print(two_strings(100, 'python')) # 0
print(two_strings(100, 200)) # 0
print(two_strings('python', 'python')) # 1
print(two_strings('Learn', 'py')) # 2
print(two_strings('py', 'learn')) # 3