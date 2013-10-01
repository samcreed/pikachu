# Problem 59: XOR decryption
# http://projecteuler.net/problem=59

import math
import string

def decodeMsg(msg, key):
	decoded = []
	i = 0
	for num in msg:
		decoded.append(num ^ ord(key[i]))
		i = (i + 1) % len(key)
	return decoded

def printMsg(msg, key):
	message = []
	for num in msg:
		message.append(chr(num))
	print key, "".join(message)

#################################################

msg = []
with open("cipher1.txt") as f:
	for line in f:
		nums = line.split(",")
		for num in nums:
			msg.append(int(num))

# test all possible keys
#for a in string.ascii_lowercase:
#	for b in string.ascii_lowercase:
#		for c in string.ascii_lowercase:
#			key = a + b + c
#			printMsg(decodeMsg(msg, key), key)

key = "god"
decodedMsg = decodeMsg(msg, key)

print sum(decodedMsg)

