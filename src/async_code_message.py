"""
У вас есть два списка: один с уникальными кодами, другой - с сообщениями.
Каждый код должен соответствовать определенному сообщению(при выводе сообщений
в консоль индексы элементов двух списков должны соответствовать).

1. Создайте корутину для демонстрации обратного вызова. Она должна будет выводить
на экран сообщение, соответствующее коду, и вызывать функцию для печати кода.

2. Создайте функцию, которая будет выводить на экран код.

3. Создайте корутину (точку входа main()), которая будет создавать и запускать задачи
для корутин. Каждая задача должна быть связана с определенным сообщением.

4. Используйте метод add_done_callback() для добавления обратного вызова к задаче.
Этот метод принимает функцию, которая будет вызвана, когда задача будет выполнена.
"""

import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94E", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F0"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!",
            "Всего наилучшего!"]


def print_message(message):
    print(f"Сообщение: {message}")


def print_code(code):
    print(f"Код: {code}")


async def process_code(code):
    index = codes.index(code)
    print_message(messages[index])
    print_code(code)


async def main():
    tasks = [process_code(code) for code in codes]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
