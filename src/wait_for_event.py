"""
Написать код, который имитирует работу системы безопасности. Эта система включает
в себя несколько датчиков движения (5), каждый из которых имеет уникальный
идентификатор и IP-адрес. Датчики постоянно мониторят окружающую среду
(ждут события event()), и как только обнаруживается движение, они активируются
и выводят соответствующее сообщение.

1. Создайте 5 корутин-датчиков.

2. Создайте корутину-событие, которая устанавливает событие alarm с помощью
asyncio.Event() и описанными ранее методами. Событие должно наступить
в течение 5 секунд после запуска программы.

3. После наступления event напечатайте в консоль уведомление о его срабатывании.
"""


import asyncio
import random

ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]

# Предполагаем, что у нас уже есть цикл событий
loop = asyncio.get_event_loop()

# Создаем список событий, по одному для каждого IP-адреса
events = [asyncio.Event() for _ in range(len(ip))]


# Определяем корутину для ожидания события для конкретного IP-адреса
async def wait_for_event(index):
    print(f'Датчик {index} IP-адрес {ip[index]} настроен и ожидает срабатывания')
    sleep_time = random.randint(1, 3)
    await asyncio.sleep(sleep_time)
    # Ожидаем событие
    await events[index].wait()
    print(f'Датчик {index} IP-адрес {ip[index]} активирован через {sleep_time} сек. "Wee-wee-wee-wee"')


# Определяем корутину для установки всех событий
async def set_event():

    print('Датчики зафиксировали движение')
    # Устанавливаем все события
    for event in events:
        event.set()


async def main():
    tasks = []
    for index in range(len(ip)):
        task = loop.create_task(wait_for_event(index))
        tasks.append(task)

    task = loop.create_task(set_event())
    tasks.append(task)

    await asyncio.gather(*tasks)


# Запускаем основную функцию в текущем цикле событий
loop.run_until_complete(main())
