# two_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)


def two_sum(numbers, target):
    diff_dict = {}

    for index, number in enumerate(numbers):
        difference = target - number
        if difference in diff_dict:
            return [number, difference]
        else:
            diff_dict[number] = index

    return []
