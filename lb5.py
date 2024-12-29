import random, time, csv, os
def clear_file():
    with open("New.csv", "w") as file:
        pass

def _write_data(data):
    file_not_exists = os.path.exists("New.csv") and os.stat("New.csv").st_size == 0
    with open("New.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        if file_not_exists:
            writer.writerow(["type", "time", "compare", "assign", "elements"])
        writer.writerow(data)

def _sort_arr(array, type, el):
    start = time.time()
    assign, compare = 0, 0
    for el in range(len(array)):
        value, pastIndex = array[el], el-1
        while pastIndex >= 0 and value<array[pastIndex]:
            compare += 1
            array[pastIndex + 1] = array[pastIndex]

            pastIndex -= 1
        array[pastIndex + 1] = value
        assign += 1
    end = time.time()
    ftime = round(end-start, 7)
    print(f"array = {array}\ntype = {type}, time = {ftime}, compare = {compare}, assign = {assign}")
    data = [type, ftime, compare, assign, el+1]
    _write_data(data)

def gen_array():
    clear_file()
    for el in [10, 100, 1000, 5000, 10000]:
        array = []
        print(f"\nelements = {el}")
        for ch in range(3):
            if ch == 0:
                array = list(range(el))
                type ="rising"
            elif ch == 1:
                array = list(range(el, 0, -1))
                type = "falling"
            else:
                array = list(random.choices(range(0, el), k=el))
                type = "random"
            _sort_arr(array, type, el)
gen_array()
