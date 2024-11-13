# a = 10
# b = 20
# print (a + b)
# words = "I like apples"
# print(words.replace("apples", "bananas"))
# words = "Hello World"
# print(words.find("World")
# empty_list = {}

# my_list = ["apple, 42, true, 3.14"]

# print(my_list[0])
# numbers = [1,2,3,4,5]
# numbers.append(6)
# print(numbers)

# numbers = [1,2,3,4,5]

# numbers.insert(2, "hej")
# print(numbers)

# fruits = ["apple", "banana", "melon", "cherry"]
# fruits.remove("melon")
# print(fruits)

# fruits = ["apple", "banana", "melon", "cherry, pear"]

# print(fruits[:3])

# numbers = [2,7,4,5,1]
# print(sum(numbers))

# empty_dict = {}

# person = {"name": "Bobbo", "age": 37, "city": "Linköping"}

# print(person["name"])

# person = {"name": "Bobbo", "age": 37, "city": "Linköping"}

# print(person.get("proffession", "Unknown"))
# person["age"] = 26
# print(person)

# person ["proffession"] = "Hacker"
# print(person)

# age = person.pop("age")
# print("age")
# print("person")

# del person ["name"]
# print(person)

# person["proffession"] = "Hacker"
# print(person)

# key, value = person.popitem()
# print(key, value)
# print(person)

# empty_tuple = ()

# small_tuple = (5,)

# fruits = "apple", "melon", "cherry"
# print(fruits)
# print(type(fruits))

# fruits = ("apple", "melon", "cherry")
# print(fruits[0])
# print(fruits[-1])

# fruits = ("apple", "melon", "cherry")
# fruits_list = list(fruits)
# fruits_list[1] = "banana"
# fruits = tuple(fruits_list)
# print(fruits)

# empty_set = set()

# fruits = {"apple", "banana", "cherry", "apple"}

# print(fruits)

# fruits.add("grape")
# print(fruits)

# fruits.update(["orange", "mango"])
# fruits.remove("banana")
# print(fruits)

# set1 = {1,2,3}
# set2 = {3,4,5}

# union_set = set1.union(set2)
# print(union_set)

# intersection_set = set1 & set2
# print(intersection_set)

# difference_set = set1 - set2
# print(difference_set)

# symmetric = set1 ^ set2
# print(symmetric)

# frozen_fruits = frozenset (["apple", "orange", "grape"])
# print(frozen_fruits)

# x = 3 
# if x > 15:
#     print("x is greater than 15")
# elif x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than 5")

# x = 20
# if x > 10:
#     print ("above ten,")
#     if x >20:
#         print("and also above 20")
#     else:
#         print("but not above 20")

# x = 7
# y = 10
# if x > 5 and y < 15:
#     print("Both conditions are true")

# def check_a():
#     print("Kontrollerar a")
#     return False

# def check_b():
#     print("Kontrollerar b")
#     return True

# if check_a() and check_b():
#     print("Båda är sanna")
# else:
#     print("Minst en är falsk") 

# x = 5
# parity = "even" if x % 2 == 0 else "odd"
# print(f"Number är {parity}")

# a = b = c = 10
# if a == b == c:
#     print("Alla är lika")

# x = 10
# if x > 0:
#     print("x is positive")
# else:
#     pass

# number = input("Type a number")

# if number.isdigit():
#     number = int(number)
#     print(f"You typed a number {number}")
# else:
#     print("that's not a number")

# x = 5
# y = 10
# z = 15

# if (x < y and y < z) or x ==z:
#     print("True")

# def max_value(a, b):
#     if a > b:
#         return a
#     else:
#         return b
    
# biggest = max_value (10, 20)
# print(f"The biggest value is {biggest}")

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# person = ("Alice", 30, "Stockholm")
# name, age, city = person
# print(name)
# print(age)
# print(city)

# people = [("Alice", 30, "Stockholm"), ("Bob", 25, "Göteborg")]
# for name, age, city in people:
#     print(f"Name: {name}, Age: {age}, Stad: {city}")

# person = {"name": "Alice", "age": 30, "city": "Stockholm"}
# for key, value in person.items():
#     print(f"{key}: {value}")

# text = "Hello"
# for bokstav in text:
#     print(bokstav)

# fruits = {"apple", "banana", "cherry"}
# for fruit in fruits:
#     print(fruit)

# for i in range (5):
#     print(i)

# for i in range (2, 10, 2):
#     print(i) 

# for i in range(3):
#     for j in range(2):
#         print(f"i: {i}, j: {j}")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if (i) & 2 == 0:
#         continue
#     print(i)

# x = 0
# while x < 5:
#     print(x)
#     x += 1

# while True:
#     print("This is running forever")
#     break

# x = 0
# while x < 10:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)

# x = 0
# while x < 5:
#     print(x)
#     x += 1
# else:
#     print("Loopen avslutades")

# user_input = input("Ange ett kommando:")
# print(user_input)

# while True:
#     user_input = input("Ange ett kommando:")
#     if user_input == "exit":
#         break
#     elif user_input == "5":
#         print("Du skrev 5")
#         break
#     else:
#         print("Fel input, försök igen")

# a = True
# b = False

# print (a and b)
# print (a or b)
# print(not a)

# x = 5
# print(1 < x < 10)
# print(1 < x and x < 10)

# age = int(input("Ange din ålder:"))
# if 18 <= age <= 65:
#     print("Du kan jobba")
# else:
#     print("Du kan inte jobba")

# file = open("dag1.py", "r")
# content = file.read()
# print(content)
# file. close()

# file = open("dag1.py", "r")
# line = file.readline()
# while line:
#     print(line, end='')
#     line = file.readline()
# file.close()

# file = open("dag1.py", "r")
# lines = file.readlines()
# for line in lines:
#     print(line, end='')
#     file.close()

# file = open("dag1.py", "r")
# lines = file.read().splitlines()
# print(lines)

# file = open("dag1.py", "w")
# file.write("Exempeltext \n")
# file.write("Nästa rad")
# file.close()

# List comprehension

# numbers = [1,2,3,4,5]
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(squares)

# squares = [num ** 2 for num in numbers]
# print(squares)

# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)

# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = [num for num in numbers if num % 2 == 2 == 0]
# print(even_numbers)

# numbers = [1,2,3,4,4,5]
# unique_squares = {num ** 2 for num in numbers}
# print(unique_squares)

# fruits = ["apple", "cherry", "grape"]
# fruits_lengths = {fruit: len(fruit) for fruit in fruits}
# print(fruits_lengths)

# Enumerate

# fruits = ["apple", "cherry", "grape"]
# for index, fruit in enumerate(fruits):
#     print(f"index: {index}, fruit: {fruit}")

# matrix = [
#     [1,2,3]
#     [4,5,6]
#     [7,8,9]
# ]

# for i, row in enumerate(matrix):
#     for j, value in enumearte(row):

# zip

# namn = ["Alice", "Bobbo", "Stefan"]
# age = [24, 37, 19]
# for namn, age in zip(namn, age):
#     print(f"Namn: {namn}, Ålder: {age}")

# name = input("Ange ditt namn: ")
# print(name)

# FUNKTIONER

# def fincyion_name(parametrar):
#     # kod
#     return

# def greet(name):
#     return f"Hello, {name}"

# print("test")
# print(greet("Bobbo"))

# def add(a, b):
#     return a + b

# result = add(10, 25)
# print(result)

# def greet(name="World"):
#     return f"Hello {name}"

# print(greet())
# print(greet("Bobbo"))

# def add(a, b):
#     return a + b

# def add_and_square(a, b):
#     sum = add(a, b)
#     return sum + sum

# print(add_and_square(5, 2))

# LOGIK OCH FUNKTIONER

# def categorize_age(age):
#     if age < 13:
#         return "Child"
#     elif age < 20:
#         return "Teenager"
#     elif age < 65:
#         return "Adult"
#     else:
#         return "Retiree"
    
# print(categorize_age(10))
# print(categorize_age(15))
# print(categorize_age(35))
# print(categorize_age(88))

# def add(a, b):
#     return a + b
# pair = (3, 5)
# result = add(*pair)
# print(result)

# def make_power(exponent):
#     def power(x):
#         return x ** exponent
#     return power

# result = make_power(3)

# print(result(4))

# *args **kwargs

# def function_name(*args):
#     for arg in args:
#         print(arg)

# function_name(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

# def print_info(name, *args):
#     print(f"Name: {name}")
#     for arg in args:
#         print(arg)

# print_info("Alice", 30, "Stockholm", "frans",1, 15)

# def function_name(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # Anropa funktionen med nyckelord-argument
# function_name(name="Alice", age=30, city="Stockholm")

# def print_all(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_all(1, 2, 3, name="Alice", age=30, city="Stockholm")

# def sum_numbers(*args):
#     return sum(args)

# print(sum_numbers(1, 2, 3, 4))

# def build_profile(**kwargs):
#     return kwargs

# profile = build_profile(name="Alice", age=30, job="Stockholm")
# print(profile)

# def display_info(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_info(1,2,3,4, name="Ali", age=37, job="Göteborg")

# def calculate(operation, *args, **kwargs):
#     if operation == "add":
#         return sum(args)
    
#     elif operation == "subtract":
#         result = args[0]
#         for num in args[1:]:
#             result -= num
#         return result
    
#     elif operation == "multiply":
#         result = 1
#         for num in args:
#             result *= num
#         return result
    
#     elif operation == "divide":
#         result = args[0]
#         try:
#             for num in args[1:]:
#                 result /= num
#         except ZeroDivisionError:
#             return "Can't divide by zero"
#         return result
    
#     else:
#         return "Unknown operation"

# # Testanrop
# print(calculate("add", 1, 2, 3, 4))        # Output: 10
# print(calculate("subtract", 10, 2, 3))     # Output: 5
# print(calculate("multiply", 2, 3, 4))      # Output: 24
# print(calculate("divide", 10, 2, 5))       # Output: 1.0
# print(calculate("divide", 10, 0, 5))       # Output: Can't divide by zero


# lambda arguments: expression

# add = lambda x, y: x + y
# print(add(2, 3))

# def apply_func(f, x, y):
#     return f(x,y)

# result = apply_func(lambda a, b: a * b, 4, 5)
# print(result)

# map(function, iterable)

# def square(x):
#     return x * x
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))

# print(squared_numbers)

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x * x, numbers))
# print(squared_numbers)

# filter(function, iterable)

# def is_even(x):
#     return x% 2 == 0
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(is_even, numbers))
# print(even_numbers)

# number = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, number))
# print(even_numbers)

# def check_number(num):
#     if num > 0:
#         if num % 2 == 0:
#             print(f"{num} is a positive even number")
#         else:
#             print(f"{num} is a positive odd number")
#     elif num == 0:
#         print(f"{num} is 0")
#     else:
#         print(f"{num} is a negative number")

# # Testanrop
# check_number(10)    
# check_number(-5)    
# check_number(0)     

# def print_matrix(matrix):
#     for row in matrix:
#         for element in row:
#             print(element, end=" ")
#         print()  # För att byta rad efter varje rad i matrisen

# # Skapa matrisen som en lista av listor
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Anropa funktionen för att skriva ut matrisen
# print_matrix(matrix)


# def my_function():
#     local_var = 10
#     print(local_var)

# my_function()
# print(local_var)

# global_var = 20

# def my_function():
#     print(global_var)

# my_function()
# print(global_var)

# def outer_function():
#     outer_var = "Yttre"

#     def inner_function():
#         inner_var = "inre"
#         print(outer_var)
#         print(inner_var)

#     inner_function()

# outer_function()

# x = 10

# def modify_global():
#     global x
#     x = 20

# modify_global()
# print(x)

# def outer_function():
#     x = "outer"

#     def inner_function():
#         nonlocal x 
#         x = "inner"
#         print(x)
#     inner_function()
#     print(x)
# outer_function()

# INPUT VALIDERING

# user_input = input("Ange ett nummer:")
# if user_input.isdigit():
#     user_number = int(user_input)
#     print(f"Du angav: {user_number}")
# else:
#     print("Ogiltig input")

# try:
#     user_input = input("Ange ett nummer: ")
#     user_number = int(user_input)
#     print(f"Du angav: {user_number}")
# except ValueError:
#     print("Ogiltig input")

# valid_options = ("ja", "nej", "kanske")
# user_input = input("Vill du sova?: ").lower()

# if user_input in valid_options:
#     print(f"Du valde {user_input}")
# else:
#     print("Jag förstår inte, försök igen")

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model 
#         self.year = year

#     def description(self):
#         return f"{self.year}, {self.make}, {self.model}"

# car1 = Car("Volvo", "240", 1985)
# car2 = Car("Honda", "Civic", 2017)

# print(car1.model)
# print(car1.year)
# print(car1.make)

# print(car2.model)
# print(car2.year)
# print(car2.make)

# class Animal:
#     def __init__(self,name):
#         self.name = name 

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"
    
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.speak())
# print(cat.speak())

# class Animal:
#     def __init__(self,name):
#          self.name = name 

#     def speak(self):
#          pass
    
# class Dog(Animal):
#     def __init__(self, name, breed, color):
#          super().__init__(name)
#          self.breed = breed
#          self.color = color

#     def speak(self):
#          return f"{self.name} says Woof!"

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"My name is : {self.name}, I am {self.age} years old"
    
# person1 = Person("Amir", 22)    
# print(person1)

# class DefaultDict(dict):
#     def __init__(self, default_value):
#         super().__init__()
#         self.default_value = default_value

#     def __getitem__(self, key):
#         return super().get(key, self.default_value)
    
# my_dict = DefaultDict(0)
# print(my_dict["missing key"])
# my_dict["random"] = 10
# print(my_dict["random"])

# import argparse

# parser = argparse.ArgumentParser(description="Exempel verktyg")

# parser.add_argument("name", help="Här anger du ditt namn")
# parser.add_argument("age", type=int, help="Ange din ålder här")

# parser.add_argument("-v", "--verbose", action="store_true", help="Visa detaljerad info")

# args = parser.parse_args()

# if args.verbose:
#     print(f"Hej {args.name}, du är {args.age}")
# else: 
#     print(f"Hej {args.name}")

# UNDANTAGSHANTERING
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Fel: division med 0 är inte tillåtet")
# else:
#     print(f"Resultat: {result}")
# finally:
#     print("Slut på try except")

# try:
#     with open("example.txt", "r") as file:
#         content = file.read 
# except FileNotFoundError:
#     print("Fel: Filen finns inte!")
# except Exception as 

# OS - MODULEN

# import os

# os.chdir('math_script')

# cwd = os.getcwd()
# print(cwd)

# os.mkdir('test_folder') DETTA SKAPAR KATALOG
