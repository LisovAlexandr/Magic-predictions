# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random


def print_hi(text):
    print(f'{text}')


def is_name():
    name = input('What is your name? > ').capitalize()
    if [True for char in name if char.isdigit()]:
        print(f'Interesting name. Hi, {name}')
    elif name:
        print(f'Hi, {name}')
    else:
        print('Okay, I will not name you, stranger')


answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hi, I am magic predictioner, and I know the answer to any of your questions.')
    is_name()
