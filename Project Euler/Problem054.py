# Problem 54: Poker hands
# http://projecteuler.net/problem=54

class Card:
	cardRank = {}
	cardRank["A"] = 13
	cardRank["K"] = 12
	cardRank["Q"] = 11
	cardRank["J"] = 10
	cardRank["T"] = 9
	cardRank["9"] = 8
	cardRank["8"] = 7
	cardRank["7"] = 6
	cardRank["6"] = 5
	cardRank["5"] = 4
	cardRank["4"] = 3
	cardRank["3"] = 2
	cardRank["2"] = 1

	cardRank[13] = 13
	cardRank[12] = 12
	cardRank[11] = 11
	cardRank[10] = 10
	cardRank[9] = 9
	cardRank[8] = 8
	cardRank[7] = 7
	cardRank[6] = 6
	cardRank[5] = 5
	cardRank[4] = 4
	cardRank[3] = 3
	cardRank[2] = 2
	cardRank[1] = 1

	@staticmethod
	def isAce(card):
		return card == 13 or card == "A"

	@staticmethod
	def sortedValues(values):
		return sorted([Card.cardRank[v] for v in values])


class Hand:
	handRank = {}
	handRank["RoyalFlush"] = 10
	handRank["StraightFlush"] = 9
	handRank["FourKind"] = 8
	handRank["FullHouse"] = 7
	handRank["Flush"] = 6
	handRank["Straight"] = 5
	handRank["ThreeKind"] = 4
	handRank["TwoPair"] = 3
	handRank["OnePair"] = 2
	handRank["HighCard"] = 1

	def __init__(self, hand):
		self.hand = hand
		self.values, self.suites = zip(*self.hand)
		self.values = list(self.values)
		self.suites = list(self.suites)
		self._computeRank()

	def _removeAll(self, values, rmVal):
		return [value for value in values if value != rmVal]

	def _handOrder(self, values, precidence):
		if precidence:
			handOrder = [precidence] + list(reversed(self._removeAll(values, precidence)))
		else:
			handOrder = list(reversed(values))
		
		return handOrder

	def _hasHighCard(self, values):
		return (True, self._handOrder(Card.sortedValues(values), None))

	def _hasOnePair(self, values):
		prev = None
		for value in values:
			if value == prev:
				return (True, self._handOrder(values, value))
			prev = value
		return (False, None)

	def _hasTwoPair(self, values):
		values = Card.sortedValues(values)
		hasOnePair, order1 = self._hasOnePair(values)
		if hasOnePair:
			values = self._removeAll(values, order1[0])
			hasTwoPair, order2 = self._hasOnePair(values)
			if hasTwoPair:
				order = self._handOrder(values, order2[0])
				order = [order2[0]] + [order1[0]] + order[1:]
				return (True, order)
		return (False, None)

	def _hasThreeKind(self, values):
		prev1 = None
		prev2 = None
		for value in values:
			if value == prev1 == prev2:
				return (True, self._handOrder(values, value))
			prev2 = prev1
			prev1 = value
		return (False, None)

	def _hasStraight(self, values):
		sortedValues = Card.sortedValues(values)
		relValues = []
		for value in sortedValues:
			relValues.append(value - sortedValues[0])
		if sum(relValues) == 10:
			value = sortedValues[-1]
			return (True, self._handOrder(sortedValues, value))
		else:
			return (False, None)

	def _hasFlush(self, values, suites):
		sortedValues = Card.sortedValues(values)
		prev = None
		for suite in suites:
			if not prev:
				prev = suite
			elif suite != prev:
				return (False, None)
		return (True, self._handOrder(sortedValues, None))

	def _hasFullHouse(self, values):
		values = Card.sortedValues(values)
		hasThreeKind, orderKind = self._hasThreeKind(values)
		if hasThreeKind:
			values = self._removeAll(values, orderKind[0])
			hasOnePair, orderPair = self._hasOnePair(values)
			if hasOnePair:
				order = [orderKind[0]] + orderPair
				return (True, order)
		return (False, None)

	def _hasFourKind(self, values):
		prev1 = None
		prev2 = None
		prev3 = None
		for value in values:
			if value == prev1 == prev2 == prev3:
				return (True, self._handOrder(values, value))
			prev3 = prev2
			prev2 = prev1
			prev1 = value
		return (False, None)

	def _hasStraightFlush(self, values, suites):
		sortedValues = Card.sortedValues(values)
		hasStraight, order = self._hasStraight(sortedValues)
		if hasStraight:
			hasFlush, order = self._hasFlush(sortedValues, suites)
			if hasFlush:
				return (True, self._handOrder(sortedValues, order[0]))
		return (False, None)

	def _hasRoyalFlush(self, values, suites):
		sortedValues = Card.sortedValues(values)
		hasStraightFlush, order = self._hasStraightFlush(values, suites)
		if hasStraightFlush and Card.isAce(order[0]):
			return (True, self._handOrder(sortedValues, order[0]))
		return (False, None)

	def _computeRank(self):
		result, self.order = self._hasRoyalFlush(self.values, self.suites)
		if result:
			self.rank = Hand.handRank["RoyalFlush"]
			return
		result, self.order = self._hasStraightFlush(self.values, self.suites)
		if result:
			self.rank = Hand.handRank["StraightFlush"]
			return
		result, self.order = self._hasFourKind(self.values)
		if result:
			self.rank = Hand.handRank["FourKind"]
			return
		result, self.order = self._hasFullHouse(self.values)
		if result:
			self.rank = Hand.handRank["FullHouse"]
			return
		result, self.order = self._hasFlush(self.values, self.suites)
		if result:
			self.rank = Hand.handRank["Flush"]
			return
		result, self.order = self._hasStraight(self.values)
		if result:
			self.rank = Hand.handRank["Straight"]
			return
		result, self.order = self._hasThreeKind(self.values)
		if result:
			self.rank = Hand.handRank["ThreeKind"]
			return
		result, self.order = self._hasTwoPair(self.values)
		if result:
			self.rank = Hand.handRank["TwoPair"]
			return
		result, self.order = self._hasOnePair(self.values)
		if result:
			self.rank = Hand.handRank["OnePair"]
			return
		result, self.order = self._hasHighCard(self.values)
		if result:
			self.rank = Hand.handRank["HighCard"]
			return

	def compare(self, otherHand):
		result = self.rank - otherHand.rank
		if result == 0:
			for topSelf, topOther in zip(self.order, otherHand.order):
				result = Card.cardRank[topSelf] - Card.cardRank[topOther]
				if result != 0:
					return result > 0
		return result > 0


# --- program handle ---

def p1Wins(line):
	hands = line.split(" ")
	half = len(hands) / 2
	p1, p2 = Hand(hands[:half]), Hand(hands[half:])
	return p1.compare(p2) > 0

def testHighCard():
	line = "9S 6S 5S 4X 2X 8S 7S 6S 3S 2X"
	assert(p1Wins(line))
	line = "9S 7S 6S 4X 2X 9S 7S 6S 3S 2X"
	assert(p1Wins(line))

def testOnePair():
	line = "TS TS 9S 3X 2X 8S 8S 6S 3S 2X"
	assert(p1Wins(line))
	line = "TS TS 9S 3X 2X 8S 8S AS 3S 2X"
	assert(p1Wins(line))
	line = "TS TS AS 4X 2X TS TS AS 3S 2X"
	assert(p1Wins(line))

def testTwoPair():
	line = "TS TS 9S 9X 2X 8S 8S 6S 3S 2X"
	assert(p1Wins(line))
	line = "TS TS 9S 9X 2X 8S 8S 6S 6S 2X"
	assert(p1Wins(line))
	line = "TS TS 6S 6X 2X 9S 9S 8S 8S 3X"
	assert(p1Wins(line))
	line = "TS TS 9S 9X 2X TS TS 8S 8S 3X"
	assert(p1Wins(line))
	line = "TS TS 9S 9X 4X TS TS 9S 9S 3X"
	assert(p1Wins(line))

def testThreeKind():
	line = "TS TS TS 9X 2X AS AS 6S 3S 2X"
	assert(p1Wins(line))
	line = "TS TS TS 9X 2X 8S 8S 8S 3S 2X"
	assert(p1Wins(line))
	line = "TS TS TS 9X 2X TS TS TS 3S 2X"
	assert(p1Wins(line))

def testStraight():
	line = "2S 3S 4S 5X 6X 2S 3S 4S 5X 7X"
	assert(p1Wins(line))
	line = "4S 3S 5X 6X 7x 2S 3S 4S 5X 6X"
	assert(p1Wins(line))

def testFlush():
	line = "2S 3S 5S 6S 7S 3X 4X 5X 3S 3S"
	assert(p1Wins(line))
	line = "2S 3S 5S 6S AS 3X 4X 5X 3X 3X"
	assert(p1Wins(line))
	line = "2S 3S 5S 6S AS 3X 4X 5X 3X AX"
	assert(p1Wins(line))

def testFullHouse():
	line = "2S 2S 3S 3S 3S 3X 4X 5X 3S 3S"
	assert(p1Wins(line))
	line = "6S 6S 5S 5S 5S AX AX 4S 4S 4S"
	assert(p1Wins(line))
	line = "7S 7S 5S 5S 5S 6X 6X 5S 5S 5S"
	assert(p1Wins(line))

def testFourKind():
	line = "7S 7S 7S 7S 3S AX AX AS 5S 5S"
	assert(p1Wins(line))
	line = "7S 7S 7S 7S 3S 4X 4X 4S 4S 5S"
	assert(p1Wins(line))
	line = "7S 7S 7S 7S AS 7X 7X 7S 7S 5S"
	assert(p1Wins(line))

def testStraightFlush():
	line = "7S 6S 5S 4S 3S AX AX AS AS 5S"
	assert(p1Wins(line))
	line = "7S 6S 5S 4S 3S 6X 5X 4X 3X 2X"
	assert(p1Wins(line))

def testRoyalFlush():
	line = "AS KS QS JS TS 2X 3X 4X 5X 6X"
	assert(p1Wins(line))

# -- test --
testHighCard()
testOnePair()
testTwoPair()
testThreeKind()
testStraight()
testFlush()
testFullHouse()
testFourKind()
testStraightFlush()
testRoyalFlush()

# -- prog --
wins = 0
with open("poker.txt") as f:
	for line in f:
		if p1Wins(line):
			wins += 1

print wins
