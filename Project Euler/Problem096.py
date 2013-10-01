# Problem 96: Su Doku
# http://projecteuler.net/problem=96

class Grid:
	pass #tiod

# constants
BLANK = "0"
GRID_SIZE = 9
BLOCK_SIZE = 3
ALL = set([str(i) for i in range(1, 10)])
NO_PROGRESS = 0
PROGRESS = 1


def getComponents(grid):
	rows = [[BLANK] * GRID_SIZE] * GRID_SIZE
	cols = [{} * BLOCK_SIZE] * BLOCK_SIZE
	blocks = {}

	for coordinate, entry in grid:
		r, c = zip(*coordinate)
		row[r][c] = entry
		col[c][r] = entry

		# compute block indices
		br = (int(r) - 1) / BLOCK_SIZE
		bc = (int(c) - 1) / BLOCK_SIZE

		blocks[br, bc][r, c] = entry
	
	return rows, cols, blocks


def isBlockSolved(block):
	for coordinate, entry in block:
		if entry == BLANK:
			return False
	return True


def isRowSolved(row):
	for entry in row:
		if entry == BLANK:
			return False
	return True


def isColSolved(col):
	for entry in col:
		if entry == BLANK:
			return False
	return True


def stepSolveRow(grid, ri, row, blocks):
	missing = ALL - set(row)
	if len(missing) == 0:
		return NO_PROGRESS
	if len(missing) == 1:
		entry = missing[0]
		c = row.index(entry)
		grid[ri, c] = entry

		return PROGRESS


	for entry in missing:
		pass



	pass


def stepSolveCol(grid, rows, col, blocks):
	pass


def stepSolveBlock(grid, rows, cols, block):
	pass


def solve(grid):
	rows, cols, blocks = getComponents(grid)

	solved = False
	while not solved:
		# attempt to solve through logic
		progress = 1
		while not solved and progress > 0:
			progress = 0
			solved = True
			for row in rows:
				if not isRowSolved(row):
					solved = False
					progress += stepSolveRow(grid, row, cols, blocks)
			for col in cols:
				if not isColSolved(col):
					solved = False
					progress += stepSolveCol(grid, rows, col, blocks)
			for block in blocks:
				if not isBlockSolved(block):
					solved = False
					progress += stepSolveBlock(grid, rows, cols, block)

		if not solved:
			# make a guess entry, and try to fill in more
			pass



total = 0
grid = {}
with open("sudoku.txt") as f:
	row = 0
	for line in f:
		if row != 0:
			col = 1
			for entry in line:
				grid[row, col] = entry
				col = col + 1
		row = (row + 1) % 10
		if row == 0:
			solve(grid)
			total += int(grid[1, 1] + grid[1, 2] + grid[1, 3])

print total
