from threading import Thread, Event
import time


evnt = Event()


def non_blocking(event):
    print('Non-blocking function')
    time.sleep(2)
    print('Setting event..')
    time.sleep(2)

    event.set()
    print('Event setted..')


def blocking(event):
    print('Blocking function')
    event.wait()
    print('Blocking function - continue')


thrd1 = Thread(target=blocking, args=(evnt,))

thrd2 = Thread(target=non_blocking, args=(evnt,))

thrd1.start()
time.sleep(2)

thrd2.start()

thrd1.join()
thrd2.join()
