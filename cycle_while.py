# Задание 1, задание 3 из видео
def ask_user1():
    while True:
        user_resp = input('Как дела? ')
        if user_resp == 'Хорошо':
            break
ask_user1()

# Задание 2
quest_dict = {'Как дела?': 'Хорошо!',
'Что делаешь?': 'Программирую',
'Как тебя зовут?': 'Денис',
'Сколько тебе лет?': '26',
'Ты смотрел последнюю серию "Games of thrones"?': 'Нет, у меня курс по python'
}

def ask_user():
    while True:
        user_resp = input('Ввод пользователя: ')
        if user_resp in quest_dict:
            print('Программа: {}'.format(quest_dict[user_resp]))
            break
ask_user()

# Задание 1 из видео
names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
names_1 = names.copy() # создаем копию спика так как используем метод pop
while True:
    name = names_1.pop()
    print(name)
    if names_1 == []:
        print('Валера не нашелся!')
        break
    elif name == 'Валера':
        print('{} нашелся'.format(name))
        break

# Задание 2 из видео
def find_person(find_name):
    names_2 = names.copy() # создаем копию спика так как используем метод pop
    while True:
        name = names_2.pop()
        if names_2 == []:
            print('{} не нашелся(ась)!'.format(find_name))
            break
        elif name == find_name:
            print('{} нашелся(ась)'.format(name))
            break
find_person('Катя')
find_person('Петя')

# Задание 4 из видео
def get_answer():
    return input('Введите ответ пользователю: ')

def ask_user_2():
    while True:
        user_resp = input('Вопрос пользователя: ')
        if user_resp == 'Пока!':
            break
        else:
            get_answer()

ask_user_2()