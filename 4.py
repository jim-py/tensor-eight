import time

def info_decorator(func):
    def wrapper(num):
        print(f'--- Старт программы! ---')
        func(num)
        print(f'--- Конец программы! ---')
    return wrapper

def time_decorator(func):
    def wrapper(num):
        start_time = time.time()
        func(num)
        print(f'--- {round(time.time() - start_time, 5)} сек. ---')
    return wrapper

def call_decorator(func):
    def wrapper(num):
        i = 0
        while i < num:
            if i > 2:
                print('--- Функция устала ---')
                time.sleep(1)
            func(num)
            i += 1
    return wrapper


@info_decorator
@time_decorator
@call_decorator
def funct(num):
    print('Меня вызвали!')


funct(5)
