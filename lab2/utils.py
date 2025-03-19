import os
import time
import tracemalloc
import importlib.util


def read_input(task):
    """
    Функция для чтения входных данных из файла 'input.txt'.

    Возвращает список строк без символов перевода строки.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'task{task}', 'txtf', 'input.txt'))
    with open(base_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def write_output(task, *args):
    """
    Функция для записи выходных данных в файл 'output.txt'.

    Принимает переменное количество аргументов и записывает каждый на новой строке.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'task{task}', 'txtf', 'output.txt'))
    with open(base_path, 'w') as f:
        for arg in args:
            print(arg, file=f)


def decorate(task, task_name):
    import time
    import tracemalloc

    main_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'task{task}', 'src', task_name))
    spec = importlib.util.spec_from_file_location("main_module", main_path + '.py')
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)

    tracemalloc.start()

    start = time.perf_counter()

    main_module.main()

    end = time.perf_counter()

    print("Время работы: ", end - start, "секунд")
    current, peak = tracemalloc.get_traced_memory()
    print(f"Пиковая память: {peak / 2 ** 20:.2f} MB")
    tracemalloc.stop()


def check_time_and_memory(task_func, tasknumber, *args):
    print(f"task №{tasknumber} tests")
    tracemalloc.start()
    start_time = time.time()

    task_func(*args)

    tracemalloc.stop()
    return tracemalloc.get_traced_memory()[1]//1024, time.time() - start_time
