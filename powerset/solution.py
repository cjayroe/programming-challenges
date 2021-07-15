def powerset(array, recursed=False):
    sets = []

    if not recursed:
        sets.append([])

    if len(array) == 1 and recursed:
        return array

    for index, number in enumerate(array):
        sets.append([number])
        slice = array[index + 1:]

        if slice:
            new_sets = powerset(slice, True)

            for _set in new_sets:
                if isinstance(_set, int):
                    sets.append([number] + [_set])
                else:
                    sets.append([number] + _set)

            print(sets)
    return sets