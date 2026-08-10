# What is a list?
 A list is a built-in data structure that stores an ordered collection of items. It can hold different data types (like numbers, strings, or even other lists) at the same time and is mutable, meaning you can change its contents after it is created.
# HOW DO YOU ACCESS AN ITEM IN A LIST
You access an item in a list using indexing by placing the item's position number inside square brackets [] directly after the list name.Example: my_list[2] accesses the third item.3
 # list[0] vs. list[-1]
   The difference lies in the direction of the index lookup:list[0] uses positive indexing to fetch the very first item at the start of the list.list[-1] uses negative indexing to fetch the very last item at the end of the list.
# What .append() does 
   The .append() method adds a single item to the very end of an existing list, increasing the list's total length by one.Example: If fruits = ['apple'], then fruits.append('banana') changes the list to ['apple', 'banana'].
 # .remove() vs. .pop()
   Both delete items from a list, but they look for different inputs:.remove(value) searches for and deletes the first occurrence of a specific value (e.g., .remove('apple'))..pop(index) removes and returns an item at a specific position number (e.g., .pop(0) removes the first item). If you leave the brackets empty like .pop(), it removes the last item.6
# What len() does
    The len() function counts and returns the total number of items currently stored inside the list.Example: len(['a', 'b', 'c']) will output 3.
 # HOW YOU CAN USE A FOR LOOP WITH A LIST
 You can use a for loop to step through a list item by item from start to finish. This process is called iteration, and it automatically stops once the loop reaches the end of the list
# Why Lists are Useful
    Lists are essential tools in programming because they solve the problem of managing large amounts of data efficiently.Group Related Data: They let you store hundreds of related items in a single variable instead of creating hundreds of separate variables.Maintain Order: They keep data in a specific, predictable sequence.Dynamic Flexibility: They grow or shrink automatically as your program runs and adds or removes data.Easy Automation: They pair perfectly with loops to run the same piece of code over massive collections of data instantly.
