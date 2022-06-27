# 0x08. Python - More Classes and Objects

Resources
Read or watch:

* Object Oriented Programming (Read everything until the paragraph “Inheritance” (excluded))
* Object-Oriented Programming (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
* Class and Instance Attributes
* classmethods and staticmethods
* Properties vs. Getters and Setters (Mainly the last part “Public instead of Private Attributes”)
* str vs repr


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* What are the special __str__ and __repr__ methods and how to use them
* What is the difference between __str__ and __repr__
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

## Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
## General

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc


--- TASKS

### [0. Simple rectangle](./0-rectangle.py)
* Write an empty class Rectangle that defines a rectangle:


### [1. Real definition of a rectangle](./1-rectangle.py)
* Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)


### [2. Area and Perimeter](./2-rectangle.py)
* Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)


### [3. String representation](./3-rectangle.py)
* Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)


### [4. Eval is magic](./4-rectangle.py)
* Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)


### [5. Detect instance deletion](./5-rectangle.py)
* Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)


### [6. How many instances](./6-rectangle.py)
* Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)


### [7. Change representation](./7-rectangle.py)
* Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)


### [8. Compare rectangles](./8-rectangle.py)
* Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)


### [9. A square is a rectangle](./9-rectangle.py)
* Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)

--- ADVANCED

### [10. N queens]

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

    Usage: nqueens N
        If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
        Format: see example
        You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module
    
Read: Queen, Backtracking
