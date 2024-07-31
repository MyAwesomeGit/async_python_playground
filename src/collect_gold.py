"""
В игровом мире у вас есть 10 команд, каждая из которых собирает золото.
Каждая команда может собирать золото в течение случайного времени (от 1 до 5
игровых часов включительно) и возвращать случайное количество золота (от 10 до 50
единиц включительно).

1. Создайте корутину collect_gold(), которая будет:
"Собирать золото" от 1 до 5 часов включительно (в коде 1 час равен 1 секунде).
Возвращать случайное значение собранного золота от от 10 до 50 единиц включительно.
Для генерации случайных значений используйте функцию random.randint().

2. Создайте корутину main(), в которой 10 отрядов будут отправлены на сбор золота.
После того как каждый отряд завершает сбор, выведите на экран сообщение о
собранном золоте и об его общем количестве.

3. Используйте asyncio.as_completed() для получения задач по мере их завершения.
"""


import asyncio
import random

random.seed(1)


async def collect_gold():
    amount = random.randint(10, 50)
    collection_time = random.randint(1, 5)
    await asyncio.sleep(collection_time)
    return amount


async def main():
    tasks = [asyncio.create_task(collect_gold()) for _ in range(10)]
    total = 0
    for completed_task in asyncio.as_completed(tasks):
        amount = await completed_task
        total += amount
        print(f"Собрано {amount} единиц золота.")
        print(f"Общее количество золота: {total} единиц.")


asyncio.run(main())
