from threading import Thread, Condition
from queue import Queue
import time

class Violinist(Thread):
    def __init__(self, queue_violins, queue_bow, mutex_violins, mutex_bow, name):
        Thread.__init__(self)
        self.queue_violins = queue_violins
        self.queue_bow = queue_bow
        self.mutex_violins =mutex_violins
        self.mutex_bow = mutex_bow
        self.name = name

    def run(self):
        while True:
            self.mutex_violins.acquire()
            while self.queue_violins.qsize() ==0:
                self.mutex_violins.wait()
            self.queue_violins.get()
            print('Violinist ' + self.name + ' get the violin')
            self.mutex_violins.release()

            self.mutex_bow.acquire()
            while self.queue_bow.qsize() == 0:
                self.mutex_bow.wait()
            self.queue_bow.get()
            print('Violinist ' + self.name + ' get the bow')
            self.mutex_bow.release()
            print('Violinist ' + self.name + ' is playing')

            time.sleep(1)
            self.mutex_violins.acquire()
            self.queue_violins.put('violin')
            print('Violinist ' + self.name + ' put the violin')
            self.mutex_violins.notify()
            self.mutex_violins.release()

            self.mutex_bow.acquire()
            self.queue_bow.put('bow')
            print('Violinist ' + self.name + ' put the bow')
            self.mutex_bow.notify()
            self.mutex_bow.release()


def main():
    mutex_violins = Condition()
    mutex_bow = Condition()
    queue_violins = Queue()
    queue_violins.put('V')
    queue_violins.put('V')
    queue_bow = Queue()
    queue_bow.put('B')
    queue_bow.put('B')

    v1 = Violinist(queue_violins, queue_bow, mutex_violins, mutex_bow, 'v1')
    v2 = Violinist(queue_violins, queue_bow, mutex_violins, mutex_bow, 'v2')
    v3 = Violinist(queue_violins, queue_bow, mutex_violins, mutex_bow, 'v3')
    v4 = Violinist(queue_violins, queue_bow, mutex_violins, mutex_bow, 'v4')

    v1.start()
    v2.start()
    v3.start()
    v4.start()
main()