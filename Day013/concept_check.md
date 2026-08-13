1. What is file handling in Python?
this is the process of creating, opening,writing, updating and closing files in a program
2. What does open() do?
it opens a file
3. What does "r" mean when opening a file?
it makes the file readable
4. What does "w" mean
it means write

What happens to existing content when you use it?
the files existing memory gets overwritten

5. What does "a" mean?
it means append
6. What does .write() do?
it writes inside a file
7. What does .read() do?
it reads an existing file
8. Why do we use \n when writing to a file?
we use this to put things on a new line so as not to overcrowd te former and keep things legible
9. What is the advantage of using:
with open("journal.txt", "r") as file:

instead of manually doing:

file = open("journal.txt", "r")
because it is easier to read and append

and then remembering to close it?
10. What's the difference between "w" and "a"?
write overwrites the existing memor of a file by erasing it while append just adds things to the end
11. In your own words, explain what happened when you changed "a" to "w" in your journal program.
w overwrote the exiting files while a just appened
12. Complete this:

The biggest thing I learned about file handling today is...
the difference between wrting and appending