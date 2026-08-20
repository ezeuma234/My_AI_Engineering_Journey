What is a dictionary in Python?
dictionaries store information as key value pairs

2.

What is the difference between a key and a value?
a key is th nominal part of the dictionar, it is the variable that stores the information while the key is the actual value and what we want stored

3.

How do you access the value associated with "name" in:

student = {
    "name": "Uma",
    "age": 23
}
by calling it directly student[name]
What does this do?

student["age"] = 24
this updates the age of the student to 24
5.

What is the difference between:

student.keys()
student.values()
student.items()
the first calls only the keys without the values while the second calls the values without the keys and the last one calls both keys and values

What happens when you do:

for key in student:
this calls all the keys in student
7.

Explain what this does:

for key, value in student.items():
    print(key, value)
    it prints both the keys and values in the order that has been given
8.

Why do we use .items() when we want both the key and value?
.items() gives us both the key and its corresponding value, which we can unpack into two variables.
9.

Explain this dictionary comprehension in your own words:
high_scores = {
    name: score
    for name, score in scores.items()
    if score >= 70
}
its creating another dictionary called high_scores nd the contents of the dictionary will only ne those who scored higher than 70 or 70
10.

What is the biggest difference between a list comprehension and a dictionary comprehension?
list coprehensions can be created on one line from an existing iterable while dicionary comprehension cannot be created like that

11.

Complete this:

The biggest thing I learned about dictionaries today is...
how to create dicitionary comprehensions