def productSum(array, depth=1):
    total = 0

    for item in array:
        if isinstance(item, int):
            total += item
        else:
            total += productSum(item, depth + 1)
        

    return total * depth