""" A Queue of Groceries to Put Away """

import queue

if __name__ == '__main__':

    # create a new queue object
    q = queue.Queue()
    print(q.empty())

    # put bags into the queue
    q.put('bag1')
    print(q.empty())
    q.put('bag2')
    q.put('bag3')

    # get bags from the queue in FIFO order
    print(q.get())
    print(q.get())
    print(q.get())

    # demonstrate non-blocking get
    try:
        q.get_nowait()
    except queue.Empty:
        print("Queue is empty")

    # create a new queue to hold two items
    q2 = queue.Queue(maxsize=2)
    print(q2.empty())

    # put two bags into the two-item queue
    q2.put('bag1')
    print(q2.full())
    q2.put('bag2')
    print(q2.full())

    # try to put an extra bag into the queue
    try:
        q2.put_nowait('bag3')
    except queue.Full:
        print("Queue is full")