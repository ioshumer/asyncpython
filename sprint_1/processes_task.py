import multiprocessing
from multiprocessing import Process


class Worker(Process):
    def __init__(self, func, func_args, queue):
        super(Worker, self).__init__()
        # Инициализация переменных
        self.func = func
        self.func_args = func_args
        self.queue = queue

    def run(self):
        # Вызов передаваемого метода и заполнение очереди
        result = self.func(*self.func_args)
        self.queue.put(result)


def testfunc(a, b):
    sum = a + b
    print(sum)
    return sum


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    worker = Worker(testfunc, [1, 2], queue)
    worker.start()
    worker.join()
