# DATA STRUCTURES AND ALGORITHMS: Implementation with Python

# STACK datastructure - LIFO last in, first out

stack = []

stack.append('Minecraft')       # first in and bottom item
stack.append('FifaWorldCup')
stack.append('MortalKombat')
stack.append('WWE')             # last in and topmost item

print(stack)

# remove the topmost item -> WWE
stack.pop()     # remove WWE
#stack.pop()    # remove MortalKombat

print(stack)

# # Uses of stack
# 1. undo/redo programs
# 2. back and forth movement through browser history
# 3. backtracking algorithms (maze, file directories)
# 4. calling functions (call back)