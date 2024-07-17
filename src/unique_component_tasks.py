import asyncio

status_list = [
    "Отлично", "Хорошо", "Удовлетворительно", "Средне",
    "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
    "Критично", "Катастрофически"
]

components = ["CPU", "Память", "Дисковое пространство"]


async def monitor_system_component(component):
    task_name = component
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(0.5)


async def main():
    tasks = []
    for component in components:
        task = asyncio.create_task(monitor_system_component(component), name=component)
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
