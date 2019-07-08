from threading import  Thread, Lock
import time


class Counter:
    def __init__(self):
        self._value = 0
        self._lock = Lock()

    def increase(self):
        with self._lock:
            print("Acquiring counter...")
            time.sleep(1)
            self._value += 1
        print("Releasing counter...")
        time.sleep(1)


def add_count(counter, thrd_name):
    print(f'{thrd_name} is increasing...')
    counter.increase()
    print(f'{thrd_name} finished...')


cntr = Counter()


thrd1 = Thread(target=add_count, args=(cntr, "Thrd-1"))
thrd2 = Thread(target=add_count, args=(cntr, "Thrd-2"))

thrd1.start()
thrd2.start()

thrd1.join()
thrd2.join()
