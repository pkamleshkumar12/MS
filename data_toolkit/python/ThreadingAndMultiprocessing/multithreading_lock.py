from threading import Thread, Lock

import time

database_value = 0


def increase(lock):
    global database_value
    # with context manager will  lock.acquire() and lock.release()
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(1)
        database_value = local_copy


if __name__ == "__main__":
    print("start_value", database_value)

    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value", database_value)
    print("end main")
