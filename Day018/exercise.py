history = []

history.append("Google")
history.append("YouTube")
history.append("GitHub")
history.append("ChatGPT")

for i in range(3):
    page = history.pop()
    print("Going back from:", page)

print(history)

from collections import deque
print_queue = deque()

print_queue.append("Document A")
print_queue.append("Document B")
print_queue.append("Document C")

for i in range(3):
    page = print_queue.popleft()
    print("Printing:",page)

print(print_queue)
