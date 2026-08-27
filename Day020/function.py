def add(a, b):
    return a + b

answer = add(5, 3)

print(answer)

def multiply(a, b):
    return a * b

answer = multiply(6, 4)
print(answer)

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def describe_number(number):
    status = check_number(number)
    return f"{number}" is {status}

result = describe_number(-5)

print(result)



def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(500, 3)

print(total)