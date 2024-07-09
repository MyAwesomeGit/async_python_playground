import asyncio

# Missed_files содержит список файлов, которых нет на сервере
missed_files = ['table.csv', 'image.jpg']


async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f'Файл {file_name} не найден')
    else:
        await asyncio.sleep(1)
        return f'Файл {file_name} успешно скачан'


async def main():
    files = ['table.csv', 'image.jpg', 'image.png', 'file.csv', 'file1.txt']  # Полный список файлов
    tasks = [download_file(file) for file in files]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    exceptions = [result for result in results if isinstance(result, Exception)]
    for exception in exceptions:
        print(exception)


asyncio.run(main())
