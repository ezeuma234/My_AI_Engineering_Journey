def greet(name):
    print("Hello", name)


greet("Uma")
greet("Eileen")
greet("Benjamin")


def add(a, b):
    return(a + b)
result = add(15, 25)
print(result)

def student_info(name, age, goal):
    return f"My name is {name}, I am {age} years old and my is to become an {goal}."
message = student_info("Uma", 22, "AI Engineer")
print(message)

def check_age(age):
    if age >= 18:
        return "Adult"
    elif age < 13:
        return "Child"
    else:
        age <= 18
        return "Teenager"

age = int(input("enter your age: "))
result = check_age(age)
print(result)

