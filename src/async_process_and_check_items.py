import asyncio
import random


async def process_item(item, index):
    """Корутина, обрабатывающая один элемент списка"""
    try:
        await asyncio.sleep(random.randint(0, 5))
        if item == 13 or item == 'i':
            raise ValueError(f"Элемент {item} не может быть обработан")
        print(f"Элемент соответстует условию: {item}")
    except ValueError as e:
        print(f"Элемент {index} не соответстует условию: {e}")


async def main():
    """Асинхронная функция для обработки списка элементов"""
    items = [13, 2, 13, 4, 13, 'a', 'b', 'c', 'i', 13, 6, 7, 8, 13, 10, 11, 13, 'i', 'e', 'f', 'i', 'h']
    tasks = []
    for index, item in enumerate(items):
        task = asyncio.create_task(process_item(item, index))
        tasks.append(task)

    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED, timeout=3)
    """
    Все созданные задачи ожидаются с помощью asyncio.wait() c timeout=3. 
    Все ошибки, возникшие при работе задач, сохраняются.
    Все задачи, которые не успели выполниться в заданное время, отменяются. 
    """

    failed_tasks = [task for task in done if task.exception()]
    print(f"Количество заданий, завершившихся с ошибкой: {len(failed_tasks)} из {len(done)}")
    print(f"Количество незавершенных заданий: {len(pending)}")
    print(f"Всего заданий: {len(items)}")
    for task in pending:
        task.cancel()


asyncio.run(main())
