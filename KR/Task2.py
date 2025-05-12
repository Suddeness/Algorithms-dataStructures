data = {
    0:  {'g1': 0, 'g2': 0, 'g3': 0, 'g4': 0}, #додано 0
    20:  {'g1': 16, 'g2': 12, 'g3': 15, 'g4': 24},
    40:  {'g1': 30, 'g2': 36, 'g3': 36, 'g4': 22},
    60:  {'g1': 49, 'g2': 34, 'g3': 45, 'g4': 32},
    80:  {'g1': 51, 'g2': 47, 'g3': 57, 'g4': 41},
    100: {'g1': 72, 'g2': 57, 'g3': 70, 'g4': 59},
}
investments = [0, 20, 40, 60, 80, 100] #додано 0

combinations = []
for x1 in investments:
    for x2 in investments:
        for x3 in investments:
            for x4 in investments:
                if x1 + x2 + x3 + x4 == 100:
                    combinations.append((x1, x2, x3, x4))
results = {}
for combo in combinations:
    x1, x2, x3, x4 = combo
    total = data[x1]['g1'] + data[x2]['g2'] + data[x3]['g3'] + data[x4]['g4']
    results[total]=combo
max_result = max(results)
print(f"max result {max_result}, with combination {results[max_result]}")



