stack = []

stack.append("Python")
stack.append("Java")
stack.append("C++")

stack.pop()
print(stack)


stack = []

stack.append("Book 1")
stack.append("Book 2")
stack.append("Book 3")
stack.append("Book 4")

removed = stack.pop()
removed_again = stack.pop()
print(stack)
print(removed)
print(removed_again)



from collections import deque
queue = deque()

queue.append("Uma")
queue.append("Eileen")
queue.append("Benjamin")
queue.append("John")

removedd = queue.popleft()
out = queue.popleft()

print(queue)
print(removedd)
print(out)