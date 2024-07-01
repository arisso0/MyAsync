# корутины

import asyncio


async def example_coroutine(num):
    print(f"Hello {num} from coroutine!")
    await asyncio.sleep(1)
    print(f"End {num} from coroutine!")


async def main():
    tasks = []
    for i in range(10):
        task = asyncio.create_task(example_coroutine(i))  # создаем 10 задач
        tasks.append(task)  # добавляем все задачи в список tasks
    await asyncio.gather(*tasks)  # запускаем все задачи из списка tasks

asyncio.run(main())


