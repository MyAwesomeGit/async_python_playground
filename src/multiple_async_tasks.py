import asyncio

quests = [
    {"name": "Квест на поиск сокровищ", "seconds": 10, "message": "Найди скрытые сокровища!"},
    {"name": "Побег от дракона", "seconds": 5, "message": "Беги быстрее, дракон на хвосте!"}
]


async def countdown(quest, wait_for=1):
    while quest['seconds'] > 0:
        print(f"{quest['name']}: Осталось {quest['seconds']} сек. {quest['message']}")
        quest['seconds'] -= 1
        await asyncio.sleep(wait_for)
    print(f"{quest['name']}: Задание выполнено! Что дальше?")


async def main():
    escape_tasks = []
    for quest in quests:
        escape_task = asyncio.create_task(countdown(quest))
        escape_tasks.append(escape_task)
    await asyncio.gather(*escape_tasks)


asyncio.run(main())
