                            #Background Context
OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

Read or watch the below resources in the order presented.

                            #Resources
                        ##Read or watch:

Object Oriented Programming (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet) -https://alx-intranet.hbtn.io/rltoken/i49z6HxrBGRNnixo7ZWbEQ
Object-Oriented Programming (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”) -https://alx-intranet.hbtn.io/rltoken/qz3KSn154ia4H2DPaabOzg
Properties vs. Getters and Setters -https://alx-intranet.hbtn.io/rltoken/Wy2djWXK5b4rnnYlAq_wlA
Learn to Program 9 : Object Oriented Programming -https://alx-intranet.hbtn.io/rltoken/MxIOanLf5vG5QeCWek2nqQ
Python Classes and Objects -https://alx-intranet.hbtn.io/rltoken/AoLH4xp5StrQST-Cu0Fg8w
Object Oriented Programming -https://alx-intranet.hbtn.io/rltoken/-vVnWzwR3a3X0H8Oia78Ug


                        #Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

                            ##General
Why Python programming is awesome
What is OOP
“first-class everything”
What is a class
What is an object and an instance
What is the difference between a class and an object or instance
What is an attribute
What are and how to use public, protected and private attributes
What is self
What is a method
What is the special __init__ method and how to use it
What is Data Abstraction, Data Encapsulation, and Information Hiding
What is a property
What is the difference between an attribute and a property in Python
What is the Pythonic way to write getters and setters in Python
How to dynamically create arbitrary new attributes for existing instances of a class
How to bind attributes to object and classes
What is the __dict__ of a class and/or instance of a class and what does it contain
How does Python find the attributes of an object or class
How to use the getattr function
                        
                        ##Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
                           
                            #Requirements
                            ##General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


                            TASKS

   * 0. My first square

Write an empty class Square that defines a square:

    You are not allowed to import any module

   * 1. Square with size

Write a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
Why?

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

   * 2. Size validation

Write a class Square that defines a square by: (based on 1-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
        size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        if size is less than 0, raise a ValueError exception with the message size must be >= 0
    You are not allowed to import any module

   * 3. Area of a square

Write a class Square that defines a square by: (based on 2-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
        size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Public instance method: def area(self): that returns the current square area
    You are not allowed to import any module

   * 4. Access and update private attribute

Write a class Square that defines a square by: (based on 3-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square area
    You are not allowed to import any module
Why?

Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

   * 5. Printing a square

Write a class Square that defines a square by: (based on 4-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
    You are not allowed to import any module

   * 6. Coordinates of a square

Write a class Square that defines a square by: (based on 5-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
            position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
    Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        position should be use by using space - Don’t fill lines by spaces when position[1] > 0
    You are not allowed to import any module

                            #ADVANCED TASKS

   * 7. Singly linked list

Write a class Node that defines a node of a singly linked list by:

    Private instance attribute: data:
        property def data(self): to retrieve it
        property setter def data(self, value): to set it:
            data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
    Private instance attribute: next_node:
        property def next_node(self): to retrieve it
        property setter def next_node(self, value): to set it:
            next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
    Instantiation with data and next_node: def __init__(self, data, next_node=None):
And, write a class SinglyLinkedList that defines a singly linked list by:

    Private instance attribute: head (no setter or getter)
    Simple instantiation: def __init__(self):
    Should be printable:
        print the entire list in stdout
        node number by line
    Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)
    You are not allowed to import any module
 
   * 8. Print Square instance

Write a class Square that defines a square by: (based on 6-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            size is less than 0, raise a ValueError exception with the message size must be >= 0
    Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
            position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integer
    Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        position should be use by using space
    Printing a Square instance should have the same behavior as my_print()
    You are not allowed to import any module

   * 9. Compare 2 squares

Write a class Square that defines a square by: (based on 4-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be a number (float or integer), otherwise raise a TypeError exception with the message size must be a number
            if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Instantiation with size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square area
    Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area
    You are not allowed to import any module


   * 10. ByteCode -> Python #5

Write the Python class MagicClass that does exactly the same as the following Python bytecode:

            Disassembly of __init__:
                10           0 LOAD_CONST               1 (0)
                            3 LOAD_FAST                0 (self)
                            6 STORE_ATTR               0 (_MagicClass__radius)

                11           9 LOAD_GLOBAL              1 (type)
                            12 LOAD_FAST                1 (radius)
                            15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
                            18 LOAD_GLOBAL              2 (int)
                            21 COMPARE_OP               9 (is not)
                            24 POP_JUMP_IF_FALSE       60
                            27 LOAD_GLOBAL              1 (type)
                            30 LOAD_FAST                1 (radius)
                            33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
                            36 LOAD_GLOBAL              3 (float)
                            39 COMPARE_OP               9 (is not)
                            42 POP_JUMP_IF_FALSE       60

                12          45 LOAD_GLOBAL              4 (TypeError)
                            48 LOAD_CONST               2 ('radius must be a number')
                            51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
                            54 RAISE_VARARGS            1
                            57 JUMP_FORWARD             0 (to 60)

                13     >>   60 LOAD_FAST                1 (radius)
                            63 LOAD_FAST                0 (self)
                            66 STORE_ATTR               0 (_MagicClass__radius)
                            69 LOAD_CONST               3 (None)
                            72 RETURN_VALUE

                Disassembly of area:
                17           0 LOAD_FAST                0 (self)
                            3 LOAD_ATTR                0 (_MagicClass__radius)
                            6 LOAD_CONST               1 (2)
                            9 BINARY_POWER
                            10 LOAD_GLOBAL              1 (math)
                            13 LOAD_ATTR                2 (pi)
                            16 BINARY_MULTIPLY
                            17 RETURN_VALUE

                Disassembly of circumference:
                21           0 LOAD_CONST               1 (2)
                            3 LOAD_GLOBAL              0 (math)
                            6 LOAD_ATTR                1 (pi)
                            9 BINARY_MULTIPLY
                            10 LOAD_FAST                0 (self)
                            13 LOAD_ATTR                2 (_MagicClass__radius)
                            16 BINARY_MULTIPLY
                            17 RETURN_VALUE

Tip: Python bytecode

