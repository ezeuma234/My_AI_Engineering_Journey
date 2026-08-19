# What is a list comprehension?
this lets you create a new list from an existing iterable in a single line

# What is the basic structure of a list comprehension?

[________ for ________ in ________]

Explain what each part does.
it is the expression for item in iterable

3.

What does this produce?

numbers = [1, 2, 3, 4, 5]


result = [number * 2 for number in numbers]
it produces [2,4,6,8,10]
4.

Explain the difference between:
[number for number in numbers]

and:

[number for number in numbers if number % 2 == 0]
number for number in numbers just loops through the list while the second one gets all the even numbers in the list and divides by 2
5.

What does this part do?

if number % 2 == 0
this is the part that gets the even numbers
6.

What does ** 2 mean?
gets the squares of numbers it generally means x2 x2

7.

Explain this in your own words:
[name for name, score in students if score >= 70]
going through the list of names and scores of students produce a list of students that only contains names of scorers that got a score higher or equal to 70
8.

Why did we use:

name, score

instead of just:

student

in our final exercise?
becuase we needed to use both arguments

9.

What is the difference between a list comprehension and map()?
maps let you apply the same function to all the items in a collection while list comprehension just lets you create a new list from n already existing iterable on a single line

10. Complete this:

The biggest thing I learned about list comprehensions today is...
how to create new lists and some neat tips and tricks