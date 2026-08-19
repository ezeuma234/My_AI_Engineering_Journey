numbers = [2, 4, 6, 8, 10]
def multiply_by_three(numbers):
    return numbers * 3

result = map(multiply_by_three, numbers)
print(list(result))


temperatures_c = [0, 10, 20, 30, 40]
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

result = map(celsius_to_fahrenheit, temperatures_c)
print(list(result))


names = ["uma", "eileen", "benjamin"]
def make_uppercase(names):
    return names.upper()

result = map(make_uppercase, names)
print(list(result))