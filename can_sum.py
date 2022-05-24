def can_sum(arr, target):
    numbers_needed = []
    for x in arr:
        possible_number = target - x
        if possible_number in numbers_needed:
            return [x, possible_number]
        numbers_needed.append(possible_number)
    return -1


print(can_sum([1,4,3,2,4,5,5,7,8,9], 17))