from threading import Thread

import time

threads = []
num_threads = 10


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == '__main__':

    # create processes
    for i in range(num_threads):
        p = Thread(target=square_numbers)
        threads.append(p)

    # start
    for t in threads:
        t.start()

    # join
    for t in threads:
        t.join()

    print('end main')
