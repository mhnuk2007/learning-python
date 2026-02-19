""" Customer Support Ticket Queue """

import queue

if __name__ == '__main__':

    # create a queue for incoming support tickets
    ticket_queue = queue.Queue()

    print("Is queue empty?", ticket_queue.empty())

    # customers submit tickets
    ticket_queue.put("Ticket-101")
    ticket_queue.put("Ticket-102")
    ticket_queue.put("Ticket-103")

    print("Current queue size:", ticket_queue.qsize())

    # support agent processes tickets in FIFO order
    print("Processing:", ticket_queue.get())
    print("Processing:", ticket_queue.get())
    print("Processing:", ticket_queue.get())

    # demonstrate non-blocking retrieval
    try:
        ticket_queue.get_nowait()
    except queue.Empty:
        print("No more tickets to process")

    # create a limited-capacity queue for priority tickets
    priority_queue = queue.Queue(maxsize=2)

    priority_queue.put("Priority-201")
    print("Is priority queue full?", priority_queue.full())

    priority_queue.put("Priority-202")
    print("Is priority queue full?", priority_queue.full())

    # attempt to exceed capacity
    try:
        priority_queue.put_nowait("Priority-203")
    except queue.Full:
        print("Priority queue is full")