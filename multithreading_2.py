from multiprocessing import Process, Queue
import datetime
def sum(begin, end, queue):
    result = 0
    for i in range(begin, end):
        result += i

    queue.put(result)

def main():
    queue1 = Queue()
    queue2 = Queue()

    p1 = Process(target=sum, args=(0,5000000, queue1))
    p2 = Process(target=sum, args=(5000000, 10000001, queue2))

    b1 = datetime.datetime.now()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    b2 = datetime.datetime.now()

    total = queue1.get() + queue2.get()
    print(total)
    print(b2 - b1)

if __name__ == "__main__":
    main()
