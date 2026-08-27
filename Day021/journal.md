# Day 21 Journal — Python Scope and LEGB

## What I learned

Today I learned about variable scope in Python. I learned that variables created inside a function are called local variables, while variables created outside functions can be global variables.

I learned that a local variable only belongs to the function where it was created. A local variable can have the same name as a global variable without changing the global variable.

I also learned about enclosing scope and nested functions. A nested function can access a variable from the function that contains it.

## LEGB

I learned that Python searches for variables using the LEGB rule:

- L — Local
- E — Enclosing
- G — Global
- B — Built-in

Python looks for a variable in the local scope first, then enclosing scope, then global scope, and finally built-in names.

## What I understood

One important thing I learned is that the same variable name can exist in different scopes and still represent different variables.

For example:

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
This prints:

20
10

The x inside the function is local, while the x outside the function is global.

I also learned that return is a good way to pass information out of a function instead of depending on global variables.

What I found difficult

At first, I found it confusing when different scopes had variables with the same name. I also initially had trouble understanding enclosing scope.

After tracing the code step by step, I understood that Python searches outward through the scopes when looking for a variable.

Connection to AI Engineering

Scope is important because AI programs can contain many functions that process data. Understanding where variables exist and how information moves between functions will help me write cleaner and more organized programs.

Connection to AI Engineering

Scope is important because AI programs can contain many functions that process data. Understanding where variables exist and how information moves between functions will help me write cleaner and more organized programs.

Day 21 Reflection

Today I feel more comfortable with functions and variables. I now understand that functions have their own local scope and that return can be used to move values between functions.

The biggest thing I learned today is the LEGB rule and how Python searches for variables.