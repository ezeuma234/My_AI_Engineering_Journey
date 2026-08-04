# Functions
Definition: Reusable blocks of code designed to perform a single, specific action.Purpose: Eliminate code repetition, organize logic, and make programs easier to debug.Execution: They remain dormant until explicitly invoked or "called" by name in the script.
# def
Definition: The keyword used to define a new function.Syntax: Placed at the very start of a function definition line, followed by the function name.Action: Signals to Python that the indented code block below it should be saved for later execution.
# Parameters
Definition: The variable names listed inside the parentheses of a function definition.Purpose: Act as internal placeholders or blueprints for the data the function expects to receive.Scope: They only exist and can only be used inside that specific function block.
# Arguments
Definition: The actual values or data passed into the function when you call it.Purpose: Fill in the blanks created by the parameters.Example: If def greet(name): has a parameter name, then greet("Alice") passes "Alice" as the argument.
# return
Definition: The keyword used to send a result back to the line of code that called the function.Behavior: Immediately stops the execution of the function, exiting it instantly.Default: If no return statement is written, the function automatically returns None.