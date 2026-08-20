Student = {"name": "Uma", "age": 22, "goal": "AI Engineer", "country": "Nigeria"}

print(Student["name"])
print(Student["age"])
print(Student["goal"])
print(Student["country"])

Student["country"] = "Ghana"
Student["age"] = 23
print(Student)

print(Student.keys())
print(Student.values())
print(Student.items())

for values in Student:
    print(values)

for keys in Student:
    print(keys)

for keys, values in Student.items():
    print(keys + ": " + str(values))




scores = {
    "Uma": 85,
    "John": 62,
    "Eileen": 91,
    "Ben": 45,
    "Alexander": 78
}
for name, score in scores.items(): 
    if score >=70:
     print(name + ": " + str(score))  

high_scores = {} 
for name, score in scores.items():
   if score >= 70:
    high_scores[name] = score

print(high_scores)


scores = {
    "Uma": 85,
    "John": 62,
    "Eileen": 91,
    "Ben": 45,
    "Alexander": 78
}

high_scores = {
    name: score
    for name, score in scores.items()
    if score >= 70
}

print(high_scores)


products = {
    "Laptop": 1200,
    "Phone": 800,
    "Mouse": 25,
    "Keyboard": 60,
    "Monitor": 300
}

expensive_products = {
    key: value
    for key, value in products.items()
    if value > 100
}
print(expensive_products)
