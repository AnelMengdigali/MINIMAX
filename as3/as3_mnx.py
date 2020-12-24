#Assignment 3
from as3_tree import Tree
class Result:
	def __init__(self, sol=[], val=-1000):
			self.solution = sol
			self.value = val
			
class MNX:
	def __init__(self, data_list):
		self.tree = Tree()	
		self.tree.init_tree(data_list)
		self.root = self.tree.root
		self.currentNode = None
		self.successors = []		
		return

	def terminalTest(self, node):
		assert node is not None
		return len(node.children) == 0

	def utilityChecking(self, node):
		assert node is not None
		return node.value

	def getChildren(self, node):
		assert node is not None
		return node.children

	def minimax(self):
		terminal_val = self.max_v(self.root)
		#successors = self.getChildren(self.root)
		#traversed=['A', 'B', 'E']; #example of solution_array
		res = Result();

#################  Return the solution here  #################

		traversed = []
		node = self.bfs(terminal_val) #doing bfs search for finding a node with the best terminal value

		#Backtracking a solution path from found node to obtain traversed solution array:
		while node is not None:

			traversed.append(node.Name)
			node = node.parent

		traversed.reverse()

		res.value = terminal_val #you put the best terminal value for root node here
		res.solution = traversed #you put the solution_array here

#################  Return the solution here  #################

		return res

	#BFS search for finding a node with the best termial value = Helper method
	def bfs(self, termValue):

		traversed = []
		queue = [self.root]

		while queue:

			node = queue.pop(0)

			if node.value == termValue:
				return node

			traversed.append(node)
			children = self.getChildren(node)

			for child in children:

				if child not in traversed and child not in queue:
					queue.append(child)

		return None

	def max_v(self, node):		
		if self.terminalTest(node):
			return self.utilityChecking(node)		
		max_v = -1000 #we use 1000 as the initial_maximum value --> fixed to -1000
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			max_v = max(max_v, self.min_v(deeper_node)) #min(...) --> fixed to max(...)
		return max_v

	def min_v(self, node):		
		if self.terminalTest(node):
			return self.utilityChecking(node)
		min_v = 1000 #we use -1000 as the initial_minimum value --> fixed to 1000
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			min_v = min(min_v, self.max_v(deeper_node)) #max(...) --> fixed to min(...)
		return min_v
