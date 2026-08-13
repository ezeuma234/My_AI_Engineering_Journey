with open("journal.txt", "a") as file:
    file.write("Day 13\n")
    file.write("Today i learnt a lot of things such as file manipulation and error handling and loads of other stuff.\n")

with open("journal.txt", "r") as file:
    content = file.read()
    print(content)