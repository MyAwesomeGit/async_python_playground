"""
Каждый фейерверк должен сгенерировать два сообщения:

1. Первое сообщение выводится при "запуске" фейерверка. Оно должно содержать
информацию о цвете, форме и действии фейерверка в формате:
f"Запущен {color} {shape} салют, в форме {action}!!!",
где {color}, {shape} и {action} - это одно из значений свойств фейерверка.

2. Второе сообщение выводится по истечении времени полета фейерверка и сообщает о его
"завершении". Оно должно быть в формате: f"Салют {color} {shape} завершил выступление {action}",
где {color}, {shape} и {action} также берутся из списка свойств фейерверка.

Используйте функцию product()  из модуля itertools для создания декартова произведения
всех возможных комбинаций форм, цветов и действий. Всего должно получиться 75 уникальных комбинаций.

Определите асинхронную функцию launch_firework(), которая принимает данные о комбинации
значений салюта, эта функция должна:

Выводить сообщение о запуске фейерверка с указанием его цвета, формы и действия.
f"Запущен {color} {shape} салют, в форме {action}!!!"
"Замораживать" выполнение функции launch_firework() на время полета фейерверка,
используя asyncio.sleep(), на рандомное значение, например от 1 до 5 сек.
await asyncio.sleep(random.randint(1, 5))
Выводить сообщение о завершении выступления фейерверка.
f"Салют {color} {shape} завершил выступление {action}"
Определите асинхронную функцию (точку входа)main(), которая создает список задач,
используя корутину launch_firework() для каждого фейерверка, и ожидает завершения всех задач,
используя asyncio.gather().
"""

import asyncio
from itertools import product
import random

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]

combinations = list(product(shapes, colors, actions))


async def launch_firework(color, shape, action):
    print(f"Запущен {shape} {color} салют, в форме {action}!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {shape} {color} завершил выступление {action}")


async def main():
    tasks = [launch_firework(*combo) for combo in combinations]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
