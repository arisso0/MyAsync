`asyncio.run(coro, *, debug=None, loop_factory=None)`
функция создаёт цикл событий и запускает указанную корутину  в нём.
После завершения выполнения coro автоматически закрывает цикл событий.

`asyncio.sleep(delay, result=None)` — функция приостанавливает выполнение на delay секунд.

`asyncio.create_task(coro, *, name=None, context=None)` — функция оборачивает coro в объект Task,
т.е. она будет запланирована для выполнения в цикле событий.

`asyncio.wait_for(aw, timeout)` — функция ожидает завершения aw(awaitable объект) и,
если выполнение не завершено в течение timeout секунд, вызывается TimeoutError.

`asyncio.gather(*aws, return_exceptions=False)` — функция запускает awaitable объекты,
переданные в функцию, как последовательность *aws, и собирает результаты их работы.

`asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)` — функция запускает Task и Future
из итерируемого aws , до выполнения условия, указанного в return_when,
возвращает кортеж из двух множеств Task/Future в виде (done, pending).
Это позволяет вам узнать, какие задачи были выполнены и какие еще ожидают выполнения.

`asyncio.ensure_future(coro_or_future, *, loop=None)` DEPREC —  обеспечивает обертывание корутин и
других awaitable объектов в объект Task, который можно использовать для отслеживания
состояния асинхронной операции.

`asyncio.run_coroutine_threadsafe(coro, loop)` — используется для отправки корутины в заданный
цикл событий (event loop) таким образом, чтобы это было безопасно в условиях многопоточности.

`asyncio.shield(aw)` — функция защищает aw (awaitable объект) от отмены.
asyncio.new_event_loop() — функция создает и возвращает новый объект цикла событий.

`asyncio.set_event_loop(loop)` — функция устанавливает loop в качестве текущего цикла событий
для текущего потока ОС, если в нем нет уже запущенного цикла событий.

`loop.run_until_complete(future)` — метод позволяет запустить выполнение корутины или объекта
Future внутри цикла событий.

`asyncio.get_event_loop()` — функция возвращает текущий цикл событий .

`asyncio.get_running_loop()` — функция возвращает текущий запущенный цикл событий в текущем
потоке ОС. Вызывает исключение RuntimeError, если нет запущенного цикла событий.