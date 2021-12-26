from threading import Lock
lock = Lock()

"""
lock.acquire()
 # some thread safe code
lock.release()

using with
with lock:
    # thread safe code
"""

