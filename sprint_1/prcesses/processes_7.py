# python 3.9.5

import multiprocessing


def calculate_func(data):
    result = data * 2 + 44
    return result


def callback(result):
    print(result)


if __name__ == '__main__':
    inputs = list(range(0, 100))

    # Использование map
    pool = multiprocessing.Pool(processes=3)
    pool_outputs = pool.map(calculate_func, inputs)
    pool.close()
    pool.join()
    print('Pool:', pool_outputs)

    # Использование apply_async
    pool2 = multiprocessing.Pool(processes=3)
    for num in inputs:
        pool2.apply_async(calculate_func, (num,), callback=callback)
    pool2.close()
    pool2.join()
