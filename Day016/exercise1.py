numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]
print(doubled)


numbers = [3, 6, 9, 12, 15]

tripled = [number * 3 for number in numbers]
print(tripled)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [number for number in numbers if number % 2 == 0]
print(even)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

special_figs = [number ** 2 for number in numbers if number % 2 == 0]
print(special_figs)


numbers = [3, 7, 10, 12, 15, 20, 25, 30]

speciall_figs = [number ** 2 for number in numbers if number > 10]
print(speciall_figs)

names = ["Uma", "John", "Eileen", "Ben", "Alexander"]

char_4 = [name for name in names if len(name) > 4]
print(char_4)


students = [
    ("Uma", 85),
    ("John", 62),
    ("Eileen", 91),
    ("Ben", 45),
    ("Alexander", 78)
]

high_scorers = [name for name, score in students if score >= 70 ]
print(high_scorers)