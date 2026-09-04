def greet():
    message = "Hello"
    print(message)
# message is a local variable because it was created inside greet().

greet()

def greet():
    message = "Hello"


greet()
print(message )
#This produces an error because message only exists inside greet().

name = "Uma"


def greet():
    print(name)


greet()
#name is global, so the function can read it.

x = 10


def test():
    x = 20
    print(x)


test()

print(x)
# There are two different x variables.

def multiply(a, b):
    result = a * b
    return result


answer = multiply(5, 3)

print(answer)
#Inside the function:
#a = 5
#b = 3
#result = 15
#Those variables belong to the function.

def outer():
    message = "Hello from outer"

    def inner():
        print(message)

    inner()


outer()
#inner() doesn't have message, so Python looks in the enclosing function outer().

score = 10


def increase_score():
    global score
    score = score + 5


increase_score()

print(score)
#Python would treat score inside the function as a local variable when you assign to it.