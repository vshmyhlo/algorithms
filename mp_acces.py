import os
import random
import time
from multiprocessing import Process, Pipe, Queue


class Cache(object):
    def __init__(self):
        self.task_q = Queue()
        self.p = Process(target=self.loop, args=(self.task_q,))
        self.p.start()

    def __setitem__(self, key, value):
        recv_c, send_c = Pipe(duplex=False)

        pid = os.getpid()
        self.task_q.put((pid, send_c))
        time.sleep(random.uniform(0, 0.1))
        res = recv_c.recv()

        print('match: {}'.format(pid == res))

    def join(self):
        self.task_q.put(None)
        self.p.join()

    @staticmethod
    def loop(task_q):
        while True:
            req = task_q.get()

            if req is None:
                break

            data, send_c = req
            send_c.send(data)


def worker(cache):
    for _ in range(10):
        cache[random.choice(list('abcdefg'))] = random.randint(0, 9)


cache = Cache()

ps = [Process(target=worker, args=(cache,)) for _ in range(10)]
for p in ps:
    p.start()
for p in ps:
    p.join()
print('ps joined')
cache.join()
print('cache joined')
