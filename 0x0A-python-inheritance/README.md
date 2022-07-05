# 0x0A. Python - Inheritance

## Resources
## Read or watch:

* Inheritance
* Multiple inheritance
* Inheritance in Python
* Learn to Program 10 : Inheritance Magic Methods

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes 
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use isinstance, issubclass, type and super built-in functions


## Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
## Python Scripts

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

## Python Test Cases

Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Documentation
Do not use the works import or from inside your comments, the checker will think you try to import some modules


--- ##MANDATORY

### [0. Lookup](./0-lookup.py)
* Write a function that returns the list of available attributes and methods of an object:


### [1. My list](./1-my_list.py)
* Write a class MyList that inherits from list:


### [2. Exact same object](./2-is_same_class.py)
* Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.


### [3. Same class or inherit from](./3-is_kind_of_class.py)
* Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.


### [4. Only sub class of](./4-inherits_from.py)
* Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.


### [5. Geometry module](./5-base_geometry.py)
* Write an empty class BaseGeometry.


### [6. Improve Geometry](./6-base_geometry.py)
* Write a class BaseGeometry (based on 5-base_geometry.py).


### [7. Integer validator](./7-base_geometry.py)
* Write a class BaseGeometry (based on 6-base_geometry.py).


### [8. Rectangle](./8-rectangle.py)
* Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).


### [9. Full rectangle](./9-rectangle.py)
* Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)


### [10. Square #1](./10-square.py)
* Write a class Square that inherits from Rectangle (9-rectangle.py):


### [11. Square #2](./11-square.py)
* Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).

--- ##ADVANCED

### [12. My integer](./100-my_int.py)
* Write a class MyInt that inherits from int:


### [13. Can I?](./101-add_attribute.py)
* Write a function that adds a new attribute to an object if it’s possible:

---