x = [5, 8, 5, 8, 5, 8, 50]
y = [40, 0, 5, 3, 4, 5, 10]


def minimum_cars_needed(capacity, seated):
    capacity_list, seated_list = zip(*sorted(zip(capacity, seated), reverse=True, key=lambda x: x[0]))
    cars_needed = 0
    total_people = sum(seated_list)
    cur = 0
    while total_people > 0:
        cars_needed += 1
        total_people -= capacity_list[cur]
        cur += 1
    return cars_needed
print(minimum_cars_needed(x, y))