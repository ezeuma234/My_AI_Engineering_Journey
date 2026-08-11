Dictionary
A Python dictionary is a built-in data structure that stores data in unordered, mutable, and indexed collections of key-value pairs. They act like real-world dictionaries, where you look up a unique word (the key) to find its definition (the value).
Key-Value Pairs
Every item in a dictionary consists of a key and a corresponding value.Keys must be unique and immutable data types, such as strings, numbers, or tuples.Values can be any data type, including lists, integers, or even other dictionaries, and they can repeat
Accessing Values
You can access a value by referencing its key inside square brackets []. Alternatively, use the .get() method to avoid an error if the key does not exist
Adding and Updating Values
Adding a brand-new key-value pair and updating an existing one use the exact same syntax: dictionary[key] = value. If the key exists, its value is overridden; if it does not, a new pair is created.
Deleting Items (del vs .pop())
del statement: Permanently deletes a key-value pair using the key. It raises a KeyError if the key is missing..pop() method: Removes the key-value pair and returns the value so you can save or print it. You can provide a fallback default value to prevent errors
Checking Keys with in
The in keyword checks if a specific key is present in the dictionary, returning True or False. This does not search the dictionary's values, only its keys
Looping Through Dictionaries
You can loop through a dictionary to read its data in a few different ways depending on what you need.like Looping via .items() (Keys and Values)This is the most common approach. The .items() method breaks each entry down into a key-value tuple, allowing you to unpack them into two variables at once


