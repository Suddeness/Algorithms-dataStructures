import random
def Main():
    Hash = {}
    N = 21*5+50
    S = N*0.75
    for i in range(N):
        key = f"key{i}"
        value = random.randint(1, 100)
        Hash[key]=value
    print(Hash)
    for el in list(Hash.keys()):
        if Hash[el]%2==0:
            del Hash[el]
    print(Hash)

Main()