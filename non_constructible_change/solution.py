# [5, 7, 1, 1, 2, 3, 22]
# [1, 1, 2, 3, 5, 7, 22]
# 20

# [1, 1, 2, 5]
# 4


def non_change(change: list):
    change.sort()
    min_change_not_made = 0

    for coin in change:
        if coin > min_change_not_made + 1:
            return min_change_not_made + 1

        min_change_not_made += coin
        
    return min_change_not_made + 1

