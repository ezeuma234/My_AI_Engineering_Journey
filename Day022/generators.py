def countdown(start):
    while start > 0:
        yield start
        start -= 1

for n in countdown(3):
    print(n)  # 3, 2, 1


def example():
    print("A")
    yield 1

    print("B")
    yield 2

    print("C")
    yield 3

x = example()

print(next(x))
print(next(x))
print(next(x))
print(next(x))