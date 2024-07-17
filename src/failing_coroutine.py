import asyncio


async def failing_coroutine():
    await asyncio.sleep(1)
    raise ValueError("Возникла ошибка в корутине failing_coroutine()")


async def successful_coroutine():
    await asyncio.sleep(1)
    print("Успешное выполнение successful_coroutine()")


async def main():
    tasks = [asyncio.create_task(failing_coroutine()), asyncio.create_task(successful_coroutine())]
    try:
        await asyncio.gather(*tasks)
    except ValueError as ex:
        print(ex)

    for i, task in enumerate(tasks, start=1):
        # Получаем исключение из задачи, если оно возникло, и выводим информацию о нем
        exc = task.exception()
        if exc:
            print(f"Задача {i}: Исключение - {exc}")
        else:
            print(f"Задача {i}: Успешно выполнена")


if __name__ == "__main__":
    asyncio.run(main())
