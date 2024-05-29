import asyncio
import time


# Первое сообщение от корутины 1
# Первое сообщение от корутины 2
# Первое сообщение от корутины 3
# Второе сообщение от корутины 3
# Второе сообщение от корутины 2
# Второе сообщение от корутины 1
# Третье сообщение от корутины 2
# Третье сообщение от корутины 3
# Третье сообщение от корутины 1
# Четвертое сообщение от корутины 1
# Четвертое сообщение от корутины 3
# Четвертое сообщение от корутины 2


async def coroutine_1(delay=0.1):
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(0.3)
    print("Второе сообщение от корутины 1")
    await asyncio.sleep(0.3)
    print("Третье сообщение от корутины 1")
    await asyncio.sleep(0.1)
    print("Четвертое сообщение от корутины 1")


async def coroutine_2(delay=0.1):
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(0.2)
    print("Второе сообщение от корутины 2")
    await asyncio.sleep(0.2)
    print("Третье сообщение от корутины 2")
    await asyncio.sleep(0.5)
    print("Четвертое сообщение от корутины 2")


async def coroutine_3(delay=0.1):
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(0.1)
    print("Второе сообщение от корутины 3")
    await asyncio.sleep(0.4)
    print("Третье сообщение от корутины 3")
    await asyncio.sleep(0.3)
    print("Четвертое сообщение от корутины 3")


async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )

start_t = time.time()
asyncio.run(main())
print({time.time()-start_t})
