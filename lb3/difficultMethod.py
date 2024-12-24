import random

class HashTable:
    def __init__(self, size):
        self.data = [[] for _ in range(size) ]
        self.size = size

    def set(self, key, value):
        index = hash(key) % self.size
        backet = self.data[index]
        for i, (k,v) in enumerate(backet):
            if k == key:
                backet[i] = (key,value)
                return
        backet.append((key,value))

    def get(self, key, user=True):
        index = hash(key) % self.size
        backet = self.data[index]
        for i, (k,v) in enumerate(backet):
            if k == key:
                if user:
                    return (f"key: {k}, value: {v}")
                return (i, index)
        print("key not found")
        return None

    def remove(self, key):
        res = self.get(key,False)
        if res:
            i, index = res
            del self.data[index][i]
            print("deleted")

    def show(self):
        ss = []
        for bucket in self.data:
            for key, value in bucket:
                ss.append(f"{key}: {value}")
        print(ss)

    def minusEven(self):
        for bucket in self.data:
            for i in range(len(bucket) - 1, -1, -1):
                if bucket[i][1] % 2 == 0:
                    del bucket[i]
def Main():
    N = 21*5+50
    S = N*0.75
    newt = HashTable(int(S))
    for i in range(N):
        key = f"key{i}"
        value = random.randint(1, 100)
        newt.set(key, value)

    newt.show()
    newt.minusEven()
    print("")
    newt.show()

Main()
