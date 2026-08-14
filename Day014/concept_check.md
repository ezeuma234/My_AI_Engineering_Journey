1. What is a Module?A module is simply a Python file containing code (variables, functions, or classes) that you can reuse in other files. It has a .py extension.
2. What Import DoesThe import keyword loads the code from a module into your current file so you can use its contents without rewriting them.
3. Difference Between Importsimport calculator: Loads the entire module. You must type calculator.add() to use its tools.from calculator import add: Pulls only the specific add function into your file. You can use it directly as add().
4. Why We Use ModulesOrganization: Keeps code neat and manageable.Reusability: Allows you to use the same code in multiple projects.Collaboration: Lets different team members work on separate files easily.Maintainability: Makes finding and fixing bugs much quicker.
5. Breakdown of calculator.add(10, 5)calculator: The name of the module (the file) you imported.. (Dot operator): The connector that tells Python to look inside that module.add(): The specific function inside the module that you are running.

6. Why Use student1.introduce() Directly?We use student1.introduce() because the function itself already contains a print() statement inside its definition. If you wrap it in another print(), Python will execute the function (printing the introduction) and then print None because the function doesn't return a value.
7. What w vs a Does
w (Write mode): Overwrites the file. It deletes everything inside your Day 13 journal and replaces it with the new text.
a (Append mode): Adds new text to the end of the file without deleting your past entries.

8. Complete the SentenceThe biggest thing I learned about modules and imports today is that they act like digital toolboxes, allowing us to keep our main code clean by neatly organizing our tools into separate files.