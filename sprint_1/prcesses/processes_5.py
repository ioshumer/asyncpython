# python 3.9.5

import multiprocessing


def custom_func(i):
    print('Вызов функции для процесса: %s' % i)
    for j in range(0, i):
        print('\tВывод функции:%s' % j)


if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=custom_func, args=(i,))
        process.start()
        process.join()
