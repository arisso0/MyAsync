import asyncio

places = [
   "начинает путешествие",
   "находит загадочный лес",
   "переправляется через реку",
   "встречает дружелюбного дракона",
   "находит сокровище"]

roles = ["Искатель приключений", "Храбрый рыцарь", "Отважный пират"]


async def counter(name):
    for place in places:
        await asyncio.sleep(1)
        print(f"{name} {place}...")


async def countdown(name, seconds):
    if name == 'Квест на поиск сокровищ':
        text = "Найди скрытые сокровища!"
    else:
        text = "Беги быстрее, дракон на хвосте!"
    while seconds > 0:
        print(f"{name}: Осталось {seconds} сек. {text}")
        await asyncio.sleep(1)
        seconds -= 1
    print("Задание выполнено! Что дальше?")

news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Рынки акций растут на фоне новостей о вакцине",
    "Конференция разработчиков игр пройдет онлайн",
    "Открыт новый вид подводных животных"
]


async def analyze_news(keyword, news_list, delay):
    for news in news_list:
        if keyword.lower() in news.lower():
            print(f"Найдено соответствие для '{keyword}': {news}")
            await asyncio.sleep(delay)


async def monitor_cpu(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
        await asyncio.sleep(0.1)


async def monitor_memory(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
        await asyncio.sleep(0.1)


async def monitor_disk_space(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
        await asyncio.sleep(0.1)


async def main():
    # first task
    # tasks = [asyncio.create_task(counter(role)) for role in roles]
    # await asyncio.gather(*tasks)

    # second task
    # treasure_hunt = asyncio.create_task(countdown('Квест на поиск сокровищ', 10))
    # dragon_escape = asyncio.create_task(countdown('Побег от дракона', 5))
    #
    # await treasure_hunt
    # await dragon_escape

    # third task
    # keywords = ["COVID-19", "игр", "новый вид"]
    # tasks = [asyncio.create_task(analyze_news(i, news_list, 1)) for i in keywords]
    # await asyncio.gather(*tasks)

    # forth task
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]
    t1 = asyncio.create_task(monitor_cpu(status_list), name="CPU")
    t2 = asyncio.create_task(monitor_memory(status_list), name='Память')
    t3 = asyncio.create_task(monitor_disk_space(status_list), name='Дисковое пространство')

    await asyncio.gather(*[t1, t2, t3])

asyncio.run(main())
