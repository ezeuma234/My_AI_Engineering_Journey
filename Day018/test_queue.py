from collections import deque

print("TEST STARTED")

queue = deque(["Uma", "John"])

print("QUEUE:", queue)

x = queue.popleft()

print("X:", x)

print("QUEUE AFTER:", queue)