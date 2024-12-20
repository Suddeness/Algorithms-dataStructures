import random
from collections import deque

class Queue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def enqueue(self, item):
        if len(self.queue) < self.size:
             self.queue.append(item)
        else:
            raise OverflowError

    def dequeue(self):
        if not self.isempty():
            return self.queue.popleft()
        else:
            raise IndexError

    def front(self):
        if not self.isempty():
            return self.queue[0]
        else:
            raise IndexError

    def isfull(self):
        return len(self.queue) == self.size

    def isempty(self):
        return len(self.queue)==0

    def __str__(self):
        return str(self.queue)

    def isprime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def Main():
    S = 21*5+50
    queue = Queue(S)
    for _ in range(S):
        num = random.randint(1, 1000)
        queue.enqueue(num)
    prime = [el for el in queue.queue if queue.isprime(el)]
    print(prime)
Main()
