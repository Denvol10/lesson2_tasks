"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
answers = {
    'привет': 'Привет!',
    'как дела': 'Отлично, а у тебя?',
    'пока': 'Еще увидимся'
}

def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        try:
            user_input = input('Скажи что-нибудь: ')
            answer = get_answer(user_input, answers)
            print(answer)
            if user_input == 'пока':
                break
        except KeyboardInterrupt:
            print('\nПока')
            break

if __name__ == "__main__":
    ask_user(answers)