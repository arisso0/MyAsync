# Ваша задача: дополнить функцию main(),
# чтобы три студента — Алекс, Мария и Иван — могли читать книги асинхронно.
# Все студенты начинают читать, но из-за различной скорости чтения
# заканчивают чтение они в разное время.
# Используя асинхронное программирование и функцию asyncio.create_task(),
# вы должны сделать так, чтобы каждый студент начал и закончил чтение
# в соответствии со своим индивидуальным временем.
#
# Ваша версия функции main() должна асинхронно запустить чтение книг для этих студентов:
#
# Алекс — 5 секунд,
# Мария — 3 секунды
# Иван — 4 секунды

import asyncio
import time


# async def read_book(student, time_read):
#     print(f"{student} начал читать книгу.")
#     await asyncio.sleep(time_read)
#     print(f"{student} закончил читать книгу за {time_read} секунд.")

# Ваша задача — написать асинхронный код, который позволит всем трем студентам
# одновременно начать прохождение выбранных ими курсов и корректно рассчитает время,
# затраченное каждым из них на обучение. Время прохождения курса должно быть вычислено
# по формуле reading_time = steps / speed, где reading_time — время в часах,
# необходимое для прохождения курса.

students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}


async def study_course(student, course, steps, speed):
    print(f"{student} начал проходить курс {course}.")
    reading_time = round(steps / speed, 2)
    await asyncio.sleep(reading_time)
    print(f"{student} прошел курс {course} за {reading_time} ч.")


async def main():
    tasks = [asyncio.create_task(
        study_course(student,
                     students[student]['course'],
                     students[student]['steps'],
                     students[student]['speed'])
    ) for student in students]
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')
