"""
Using queues implemented from other module
"""

from queues import Queue

def main():
    fifo = Queue()

    fifo.enqueue("1st")
    fifo.enqueue("2nd")
    fifo.enqueue("3rd")

    print(fifo.dequeue())
    print(fifo.dequeue())
    print(fifo.dequeue())

if __name__ == "__main__":
    main()
