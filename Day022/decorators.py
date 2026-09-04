def my_decorator(function):

    def wrapper():
        print("Starting function...")
        function()
        print("Function finished!")

    return wrapper

def greet():
    print("Hello")

greet = my_decorator(greet)

greet()

# ======PYTHON SYNTAX METHOD=====

@my_decorator
def greet():
    print("Hello!")

greet = my_decorator(greet)