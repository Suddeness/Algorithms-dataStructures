import random, time, csv, os
def clear_file():
    with open("New.csv", "w") as file:
        pass
def write_data(data):
    file_not_exists = os.path.exists("New.csv") and os.stat("New.csv").st_size == 0
    with open("New.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        if file_not_exists:
            writer.writerow(["type", "time", "compare", "assign", "elements"])
        writer.writerow(data)
def gen_array():
    clear_file()
    for el in [10, 100, 1000, 5000, 10000]:
        arr = []
        print(f"\nelements = {el}")
        for ch in range(3):
            if ch == 0:
                arr = list(range(1, el+1))
                t = "rising"
            elif ch == 1:
                arr = list(range(el, 0, -1))
                t = "falling"
            else:
                arr = list(random.choices(range(1, el+1), k=el))
                t = "random"

            sorted_arr = arr[:]
            start = time.time()
            compare, assign = Merge_sort(a=sorted_arr, p=0, r=len(sorted_arr) - 1)
            end = time.time()
            if el == 10:
                print(f"array = {sorted_arr}")
            else:
                print(f"array[:10] = {sorted_arr[:10]}...array[-10:] = {sorted_arr[-10:]}")
            ftime = round(end-start, 7)
            print (f"type = {t}, time = {ftime}, compare = {compare}, assign = {assign}")
            data = [t, ftime, compare, assign, el]
            write_data(data)
def Merge_sort(a, p, r):
    compare, assign = 0, 0
    if p < r:
        q = (p + r) // 2
        c1, a1 = Merge_sort(a, p, q)
        c2, a2 = Merge_sort(a, q + 1, r)
        c3, a3 = Merge(a, p, q, r)
        compare = c1 + c2 + c3
        assign = a1 + a2 + a3
    return compare, assign
def Merge(a, p, q, r):
    left = a[p:q+1]
    right = a[q+1:r+1]
    Il, Ir = 0, 0
    compare, assign = 0, 0
    Im = p
    while Il < len(left) and Ir < len(right):
        compare += 1
        if left[Il]<=right[Ir]:
            a[Im]=left[Il]
            Il+=1
        else:
            a[Im]=right[Ir]
            Ir+=1
        Im += 1
        assign+=1
    while Il<len(left):
        a[Im] = left[Il]
        Im += 1
        Il += 1
        assign += 1
    while Ir<len(right):
        a[Im] = right[Ir]
        Im += 1
        Ir += 1
        assign += 1
    return compare, assign
gen_array()
