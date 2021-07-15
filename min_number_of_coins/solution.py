def minNumberOfCoinsForChange(target_total, coins):
    min_coins = float('inf')
    coin_count = 0

    for coin in coins:
        new_total = target_total - coin
        
        if new_total >= 0:
            coin_count += 1
            sub_coins = 0

            if new_total == 0:
                min_coins = min(min_coins, coin_count + sub_coins)

            if new_total != 0:
                sub_coins = minNumberOfCoinsForChange(new_total, coins)
                min_coins = min(min_coins, coin_count + sub_coins)
                coin_count = 0
        else:
            continue

            
    return min_coins
        
		
