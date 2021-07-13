def spiral_traverse(array):
    column_index = 0
    row_index = 0
    spiral = []
	
    while True:
        spiral.append(array[row_index][column_index])
        array[row_index][column_index] = 0

        right_valid = is_valid(array, row_index, column_index + 1)
        left_valid = is_valid(array, row_index, column_index - 1)
        down_valid = is_valid(array, row_index + 1, column_index)
        top_valid = is_valid(array, row_index - 1, column_index)           

        if right_valid and top_valid:
            row_index -= 1
        elif right_valid:
            column_index += 1
        elif down_valid:
            row_index += 1
        elif left_valid:
            column_index -= 1
        elif top_valid:
            row_index -= 1
        else:
            break
    return spiral

def is_valid(array, row_index, column_index):
    if row_index > len(array) - 1:
        return False

    if column_index > len(array[row_index]) - 1:
        return False

    if column_index < 0 or row_index < 0:
        return False

    if array[row_index][column_index] == 0:
        return False

    return True

