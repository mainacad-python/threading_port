from threading import  Thread, Lock
import time


class Account:
    def __init__(self, name, amount,):
        self._amount = amount
        self.name = name
        self._lock = Lock()


def transaction(acc1, acc2, value, thrd_name):
    print(f"{thrd_name} acquiring {acc1.name}..")
    acc1._lock.acquire()
    time.sleep(1)
    print(f"{thrd_name} acquiring {acc2.name}..")
    acc2._lock.acquire()
    time.sleep(1)
    acc1 += value
    acc2 -= value
    print(f"{thrd_name} releasing {acc1.name}..")
    acc1._lock.release()
    print(f"{thrd_name} releasing {acc1.name}..")
    acc2._lock.release()

acc1 = Account('Acc_1', 100)
acc2 = Account('Acc_2', 1001)

t1 = Thread(target=transaction, args=(acc1, acc2, 100, 'Thread-1'))
t2 = Thread(target=transaction, args=(acc2, acc1, 10, 'Thread-2'))

t1.start()
t2.start()

t1.join()
t2.join()