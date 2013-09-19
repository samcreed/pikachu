# Problem 31: Coin Sums
# http://projecteuler.net/problem=31

def coin_sum(total, target, coins):
	if total < target:
		sum = 0
		for i in range(len(coins)):
			sum += coin_sum(total + coins[i], target, coins[i:])
		return sum
	elif total > target:
		return 0
	else:
		return 1

print coin_sum(0, 200, [1, 2, 5, 10, 20, 50, 100, 200])
