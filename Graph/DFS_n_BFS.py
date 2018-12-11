from collections import defaultdict 
class Graph(object):
	"""docstring for graph"""
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,source,destination):
		self.graph[source].append(destination)

	def DFS(self,startVertex):
		len_graph = len(self.graph)
		visited = [False]*len_graph
		if startVertex not in self.graph:
			print("Vertex not present in Graph")
			return -1
		else:
			self.findNextLevel(startVertex,visited)
			for i in visited:
				if i == False:	
					self.findNextLevel(i,visited)

	def findNextLevel(self,vertex,visited):
		visited[vertex] = True
		print(vertex,end=" ")
		if len(self.graph[vertex]) == 0:
			return visited
		else:
			for i in self.graph[vertex]:
				if visited[i] == False:
					self.findNextLevel(i,visited)
	def BFS(self,vertex):
		len_graph = len(self.graph)
		visited_list = [False]*len_graph
		queue = []
		queue.append(vertex)
		visited_list[vertex] = True
		while queue:
			element = queue.pop(0)
			print(element,end=" ")
			for i in self.graph[element]:
				if visited_list[i] == False:
					queue.append(i)
					visited_list[i] = True

	# def BFS(self, s):
	# 	visited = [False] * (len(self.graph))
	# 	queue = []
	# 	queue.append(s)
	# 	visited[s] = True
	# 	while queue:
	# 		s = queue.pop(0)
	# 		print (s, end = " ")
	# 		for i in self.graph[s]:
	# 			if visited[i] == False:
	# 				queue.append(i)
	# 				visited[i] = True
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.DFS(2) #Start from node 2
print(" ")
g.BFS(2)
print(" ")
