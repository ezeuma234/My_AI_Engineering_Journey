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
