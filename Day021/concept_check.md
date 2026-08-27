1. # What is a local variable?
a local variable is a variable that exists within a function and was created within the function so as a result of that it disappears right after the particular function it is created inside is completed or has run its course

2. # What is a global variable?
a global variable is a variable that is created outside of a function

3. What does LEGB mean?
this is the rule and order python follows for finding and using variables;
L = Local
E = Enclosing
G = Global
B = Built-in

4. # What is enclosing scope?
An enclosing scope is kind of like a nested function it is a fnction that exists within a function(s) but still has its own local variable

5. # Why doesn't a local variable automatically change a global variable?
because a local variable only exists within a function and does not exist outside of it so it cannot change a global function in the hierachy of functions

6. # What does the global keyword do?
this helps to modify global variables as opposed to creating another local one

7. # Why is returning a value often preferable to using global variables?
because return is usually a cleaner way to pass data out of a function and explicit data flow is preferable to unnecessary global state