from collections import deque

customers = deque(["Uma", "John", "Eileen"])

name = input("Enter a customer name: ")

customers.append(name)

print(customers)

while customers:
    serve = customers.popleft()
    print("SERVING:", serve)

print(customers)