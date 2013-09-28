# Problem 84: Path sum: four ways
# http://projecteuler.net/problem=83

class Vertex:
	def __init__(self, name):
		self.name = name
		self.dist = float("inf")
		self.prev = None
		self.visited = False


class Edge:
	def __init__(self, u, v, length):
		self.start = u
		self.end = v
		self.length = length


def generateGraph(V, E):
	# read data into matrix
	M = {}
	r = 0
	c = 0
	with open("matrix.txt") as f:
		r = 0
		for line in f:
			c = 0
			elements = line.split(",")
			for e in elements:
				M[r, c] = int(e)
				c = c + 1
			r = r + 1

	# transform data into graph
	source = Vertex("source")
	V.append(source)
	v = Vertex((0, 0))
	E.append(Edge(source, v, M[0, 0]))

	for i in range(r):
		for j in range(c):
			u = Vertex((i, j))
			V.append(u)
			universe = [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]
			for candidate in universe:
				start, end = candidate
				if candidate in M:
					v = Vertex((start, end))
					E.append(Edge(u, v, M[start, end]))

	sink = Vertex("sink")
	V.append(sink)
	v = Vertex((r - 1, c - 1))
	E.append(Edge(v, sink, 0))


def pickSmallestVertex(V):
	minVertex = None
	for vertex in V:
		if not vertex.visited:
			minVertex = vertex
			break
	if minVertex:
		for vertex in V:
			if not vertex.visited and vertex.dist < minVertex.dist:
				minVertex = vertex

	return minVertex


def pickEdgeList(u, E):
	return [edge for edge in E if edge.start.name == u.name]


def findShortestPath(V, E, source, sink):
	for vertex in V:
		if vertex.name == source:
			vertex.dist = 0

	u = pickSmallestVertex(V)
	while u != None:
		u.visited = True
		uv = pickEdgeList(u, E)
		v = None
		for edge in uv:
			for vertex in V:
				if vertex.name == edge.end.name:
					v = vertex
					break
			if v.dist > u.dist + edge.length:
				v.dist = u.dist + edge.length
				v.prev = u
		u = pickSmallestVertex(V)

V = []
E = []
print "generating graph..."
generateGraph(V, E)
print "finding shortest path..."
findShortestPath(V, E, "source", "sink")

for e in E:
	if e.end.name == "sink":
		print e.end.dist
		break
