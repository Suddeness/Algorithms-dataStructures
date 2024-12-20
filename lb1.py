import random
from collections import deque

class Stack:
    def __init__(self, size):
        self.stack = deque()
        self.size = size

    def push(self, item):
        if len(self.stack) < self.size:
             self.stack.append(item)
        else:
            raise OverflowError

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        else:
            raise IndexError

    def peek(self):
        if not self.isempty():
            return self.stack[-1]
        else:
            raise IndexError

    def isfull(self):
        return len(self.stack) == self.size

    def isempty(self):
        return len(self.stack)==0

    def __str__(self):
        return str(self.stack)


def Main():
    S = 21*5+50
    numbers = Stack(S)
    even = Stack(S)
    odd = Stack(S)
    for _ in range(S):
        num = random.randint(1, 1000)
        numbers.push(num)
    while not numbers.isempty():
        num = numbers.pop()
        if num % 2 == 0:
            even.push(num)
        else:
            odd.push(num)
    print (f"{even}\n{odd}")

Main()
