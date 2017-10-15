# tree implementation

def tree(root, branches=[]):
	"""
	Implement the tree data structure
	"""
	for branch in branches:
		assert is_tree(branch), "branches must be tree as well"
	#list is important because we want to have the uniform representation
	return [root] + list(branches) 

def root(tree):
	"""
	return the root of the tree
	"""
	return tree[0]	

def branches(tree):
	"""
	return the branches of the tree
	"""
	return tree[1:] # You should return everything else because it contains a lot of branches

def is_tree(tree):
	"""
	check if the data structure is tree
	"""
	# if the type is not a list(formal representation of tree) 
	# 	or length is less than 1, return False
	if type(tree) != list or len(tree) < 1:
		return False
	# if every branch is not tree, return False	
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	# if it passes all the test, return True
	return True

def is_leaf(tree):
	"""
	check if the part of the tree is a leaf (degree 1)
	"""
	return not branches(tree)

def count_leaves(tree):
	"""
	count the number of leaves in the tree
	>>> count_leaves(fib_tree(4))
	5
	>>> count_leaves([1, [1]])
	1
	"""
	if is_leaf(tree):
		return 1
	else:
		return sum([count_leaves(branch) for branch in branches(tree)])

def leaves(tree):
	"""
	count the number of leaves in the tree
	>>> leaves([1, [1]])
	[1]
	>>> leaves([1, [1], [2]])
	[1, 2]
	>>> leaves(fib_tree(5))
	[1, 0, 1, 0, 1, 1, 0, 1]
	"""
	if is_leaf(tree):
		return [root(tree)]
	else:
		return sum([leaves(branch) for branch in branches(tree)], [])

def fib_tree(n):
	if n <= 1:
		return tree(n)
	else:
		left, right = fib_tree(n - 2), fib_tree(n - 1)
		return tree(root(left) + root(right), [left, right])

def increment_tree(t):
	""" 
	Return a tree like t but with leaf values increment
	>>> increment_tree([1, [1]])
	[1, [2]]
	>>> increment_tree([1, [1], [2, [3]]])
	[1, [2], [2, [4]]]
	"""
	if is_leaf(t):
		return tree(root(t) + 1)
	else:
		bs = [increment_tree(branch) for branch in branches(t)]
		return tree(root(t), bs)

def increment(t):
	"""
	Increment every value of t
	>>> increment([1, [2]])
	[2, [3]]
	>>> increment([1, [1], [2, [3]]])
	[2, [2], [3, [4]]]
	"""	
	return tree(root(t) + 1, [increment(branch) for branch in branches(t)])

def print_tree(tree, indent=0):
	"""
	Print the tree
	"""
	indent_string = ' ' * indent
	print(indent_string, root(tree))
	for branch in branches(tree):
		print_tree(branch, indent + 2)

def collect_words(t):
	if is_leaf(t):
		return root(t)
	words = []
	for b in branches(t):
		words += [root(t) + w for w in collect_words(b)]
	return words

def tree_max(t):
	if is_leaf(t):
		return root(t)
	else:
		return max([root(t)] + [tree_max(b) for b in branches(t)])

def square_tree(t):
	if is_leaf(t):
		return tree(root(t) ** 2)
	else:
		return tree(root(t) ** 2, [square_tree(b) for b in branches(t)])

def find_path(t, x):
	if root(t) == x:
		return [root(t)]
	elif is_leaf(t):
		return []
	else:
		for b in branches(t):
			print("root :", root(t))
			print("branche :", b)
			lst = [root(t)] + find_path(b, x)
			if lst[-1] == x:
				return lst
	return None

def height(t):
	if is_leaf(t):
		return 0
	return 1 + max([height(branch) for branch in branches(t)])

t = tree(1, [tree(2, [tree(3), tree(4)]), tree(5, [tree(6, [tree(7, [tree(8)])])])])