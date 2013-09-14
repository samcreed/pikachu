# http://projecteuler.net/problem=17

letters = {}
letters[1] = len("one")
letters[2] = len("two")
letters[3] = len("three")
letters[4] = len("four")
letters[5] = len("five")
letters[6] = len("six")
letters[7] = len("seven")
letters[8] = len("eight")
letters[9] = len("nine")
letters[10] = len("ten")
letters[11] = len("eleven")
letters[12] = len("twelve")
letters[13] = len("thirteen")
letters[14] = len("fourteen")
letters[15] = len("fifteen")
letters[16] = len("sixteen")
letters[17] = len("seventeen")
letters[18] = len("eighteen")
letters[19] = len("nineteen")
letters[20] = len("twenty")
letters[30] = len("thirty")
letters[40] = len("forty")
letters[50] = len("fifty")
letters[60] = len("sixty")
letters[70] = len("seventy")
letters[80] = len("eighty")
letters[90] = len("ninety")
letters[100] = len("hundred")
letters[1000] = len("thousand")

total = 0

# these appear 10 times each (190)
for i in range(1, 20):
	total += letters[i] * 10

# these appear 100 times each (900)
for i in range(1, 10):
	total += (letters[i] + letters[100]) * 100

# the word 'and' appears 891 times
total += len("and") * 891

# and the rest X20-X99 for 1 <= X <= 9
sum1_9 = sum(letters[i] for i in range(1, 10))

total += (10 * letters[20] + sum1_9) * 10
total += (10 * letters[30] + sum1_9) * 10
total += (10 * letters[40] + sum1_9) * 10
total += (10 * letters[50] + sum1_9) * 10
total += (10 * letters[60] + sum1_9) * 10
total += (10 * letters[70] + sum1_9) * 10
total += (10 * letters[80] + sum1_9) * 10
total += (10 * letters[90] + sum1_9) * 10

# and don't forget 1000
total += letters[1] + letters[1000]

print total
