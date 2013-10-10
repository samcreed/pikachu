# Problem 84: Monopoly Odds
# http://projecteuler.net/problem=84

from random import randint
from random import shuffle

class MonopolyBoard:
	# initialize board at the start of the game
	def __init__(self):
		self.squares = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1",
						"B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2",
						"D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2",
						"E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1",
						"G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2" ]

		self.communityCards = ["GO", "JAIL", 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
		shuffle(self.communityCards)
		self.communityIndex = 0

		self.chanceCards = ["GO", "JAIL", "C1", "E3", "H2", "R1", "NextR", "NextR", "NextU", "Back3"]
		shuffle(self.chanceCards)
		self.chanceIndex = 0

		self.prevDb1 = False
		self.prevDb2 = False

	def next(self, index, square):
		found = False
		while not found:
			index = (index + 1) % len(self.squares)
			found = self.squares[index].startswith(square)
		return index


	# returns the space advanced to
	def advance(self, prevSquare, dieMax):
		# calculate die roll
		prevIndex = self.squares.index(prevSquare)

		die1 = randint(1, dieMax)
		die2 = randint(1, dieMax)

		# check if we need to go to jail
		doubles = (die1 == die2)
		g2j = (doubles and self.prevDb1 and self.prevDb2)

		self.prevDb2 = self.prevDb1
		self.prevDb1 = doubles

		if g2j:
			return "JAIL"

		# determine next space to advance to
		roll = die1 + die2
		nextIndex = (prevIndex + roll) % len(self.squares)
		nextSquare = self.squares[nextIndex]

		# determine special events
		if nextSquare.startswith("CC"):
			chance = self.communityCards[self.communityIndex]
			self.communityIndex = (self.communityIndex + 1) % len(self.communityCards)
			if chance in ["GO", "JAIL"]:
				nextSquare = chance

		elif nextSquare.startswith("CH"):
			chance = self.chanceCards[self.chanceIndex]
			self.communityIndex = (self.chanceIndex + 1) % len(self.chanceCards)
			if chance in ["GO", "JAIL", "C1", "E3", "H2", "R1"]:
				nextSquare = chance
			elif chance == "NextR":
				nextSquare = self.squares[self.next(nextIndex, "R")]
			elif chance == "NextU":
				nextSquare = self.squares[self.next(nextIndex, "U")]
			elif chance == "Back3":
				nextIndex = (len(self.squares) + nextIndex - 3) % len(self.squares)
				nextSquare = self.squares[nextIndex]

		elif nextSquare == "G2J":
			return "JAIL"

		return nextSquare



# Run Monte Carlo
for j in range(7, 9):
	board = MonopolyBoard()
	turns = 10 ** j
	square = "GO"
	times = {}
	for square in board.squares:
		times[square] = 0

	print "==" * 20
	print "turns = ", turns
	print "running simulation..."
	i = 0
	while i < turns:
		if i % (turns / 100) == 0:
			print i * 100.0 / turns,

		square = board.advance(square, 6)
		times[square] += 1
		i = i + 1

	print

	ls = []
	print "simulation results:"
	for time in times:
		ls.append((times[time], time))

	ls.sort(reverse=True)
	print ls[0], ls[1], ls[2]
