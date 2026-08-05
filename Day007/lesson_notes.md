# RETURN
Definition: The keyword that exits a function and passes a calculated value back to the caller.Impact: Instantly halts the function; any code written below it on the same level is ignored.Output: Turns the function call itself into a value that can be assigned to a variable or printed.
# LOCAL SCOPE
Definition: The restricted environment inside a function where variables are created.Lifespan: Variables defined here are born when the function runs and are destroyed when it finishes.Access: Hidden from the outside world; code outside the function cannot see or use local variables.
# GLOBAL SCOPE
Definition: The outermost environment of a script, outside of any functions.Lifespan: Variables created here live for the entire duration of the program's execution.Access: Visible everywhere; both the main script and internal functions can read global variables.
# REUSING RETURNED VALUES
Definition: Capturing the output of a function by saving it into a variable for later use.Purpose: Essential for moving data out of a function's local scope into the global scope or another function.Example: Saving total = calculate_tax(100) lets you use total in future calculations later in your script.