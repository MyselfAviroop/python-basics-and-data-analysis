

#lmbda function
# addition = lambda x, y: x + y
# subtraction = lambda x, y: x - y
# multiplication = lambda x, y: x * y
# division = lambda x, y: x / y if y != 0 else "Cannot divide by zero"
# print(addition(5, 3))
# print(subtraction(5, 3))
# print(multiplication(5, 3))
# print(division(5, 3))
# print(addition(5, 0))



# map function 
# numbers1=[1,2,3,4,5]
# numbers2=[6,7,8,10]
# add=list(map(lambda x,y:x+y,numbers1,numbers2))
# print(add)



#filter function
# numbers=[1,2,3,4,5,6,7,8,9,10]
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# even_numbers=list(filter(is_even,numbers))
# print(even_numbers)
      



# from package.math import addition
# addition(5, 3)
# import os
# print(os.getcwd())
# print(os.path.dirname(__file__))
# print(os.process_cpu_count())
# print(os.listdrives())



# import shutil
# shutil.copyfile('s.txt','d.txt')


# import csv
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Age', 'City'])
#     writer.writerow(['Alice', 30, 'New York'])
#     writer.writerow(['Bob', 25, 'Los Angeles'])
#     writer.writerow(['Charlie', 35, 'Chicago'])

# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


#time module
# from datetime import datetime,timedelta
# now = datetime.now()
# print("Current date:", now.date())
# print("Current time:", now.time())
# print("Current year:", now.year)
# print("Current month:", now.month)
# yesterday = now - timedelta(days=1)
# print("Yesterday's date:", yesterday.date())






#speak text from pdf file
# import PyPDF2
# import pyttsx3

# # Initialize pyttsx3 engine for text-to-speech
# engine = pyttsx3.init()

# # Set properties (Optional: Set volume and rate)
# engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
# engine.setProperty('rate', 300)  # Speed of speech (words per minute)
# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, "rb") as file:
#         pdf_reader = PyPDF2.PdfReader(file)
#         text = ""
#         for page_num in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_num]
#             text += page.extract_text()
#     return text

# pdf_path = 'ack.pdf'  # Replace with the path to your PDF file

# # Extract text from the PDF
# text = extract_text_from_pdf(pdf_path)

# # Speak the extracted text
# if text:
#     engine.say(text)
#     engine.runAndWait()
# else:
#     print("No text found in PDF.")



# with open('s.txt', 'w+') as file:
#    file.write('Hello World\n')
#    file.write('How r u?\n')
#    file.seek(0)  # Move the cursor to the beginning of the file
#    content=file.read()
#    print(content)


#new directory
# import os
# # new_directory = 'new_package'
# # os.mkdir(new_directory)
# # print(f"Directory '{new_directory}' created successfully.")
# items = os.listdir('.')



#OOPS

#constructors and destructors
# class dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"Dog {self.name} is created.")
#     def bark(self):
#         print(f"{self.name} is barking.")
# dog1=dog("Tommy",5)
# dog2=dog("Rocky",3)
# dog1.bark() 
# print(f"Dog {dog1.name} is {dog1.age} years old.")
# print(f"Dog {dog2.name} is  {dog2.age} years old.")





# #bank account

# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount}. New balance: {self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")
#         else:
#             print("Withdrawal amount exceeds balance or is invalid.")
#     def get_balance(self):
#         return self.balance
# account= BankAccount("Avi", 10000)
# account.deposit(5000)
# account.withdraw(2000)
# account.withdraw(200)
# account.deposit(10000)





#Inheritance:It is a fundamental concept in OOP that allows a class to inherit properties and methods from another class.
# It promotes code reusability and establishes a hierarchical relationship between classes.

# class Car:
#     def __init__(self, windows, doors, engine):  # <-- double underscores
#         self.windows = windows
#         self.doors = doors
#         self.engine = engine

#     def drive(self):
#         print(f"The person will drive the {self.engine} car")

# car1 = Car(4, 4, "petrol")
# class Tesla(Car):
#     def __init__(self, windows, doors, engine, autopilot):
#         super().__init__(windows, doors, engine)
#         self.autopilot = autopilot

#     def show_autopilot(self):
#         print(f"The {self.engine} car has autopilot feature: {self.autopilot}")

# tesla1 = Tesla(4, 4, "electric", True)
# tesla1.show_autopilot()
# tesla1.drive()





#Polymorphism: It is a concept in OOP that allows objects of different classes to be treated as objects of a common superclass.
# It enables a single interface to represent different underlying forms (data type s).

# class Animal:
#     def sound(self):
#         return "Some generic animal sound"
# class dog(Animal):
#      def sound(self):
#         return "Woof! Woof!"
# class cat(Animal):
#     def sound(self):
#         return "Meow!"
# class cow(Animal):
#     def sound(self):
#         return "Moo!"       
# dog = dog()
# cat = cat()
# cow = cow()
# print(dog.sound())
# print(cat.sound())
# print(cow.sound())

# class shape:
#     def area(self):
#         return "Area of shape"
# class circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return self.radius * self.radius * 3.14
# def area_of_shape(shape):
#     return shape.area()
# circle1 = circle(10)
# print("Area of circle:", area_of_shape(circle1))





#Encapsulation: It is a concept in OOP that restricts direct access to an object's attributes and methods.
# It is achieved by using private and protected access modifiers. Encapsulation helps in data hiding and abstraction.

# class Person:
#     def __init__(self, name, age):
#         self.name = name          # public
#         self._hobby = "drawing"   # protected
#         self.__salary = 50000     # private

#     def display_info(self):
#         print(f"Name: {self.name}, Hobby: {self._hobby}, Salary: {self.__salary}")

#     def update_salary(self, amount):
#         if amount > 0:
#             self.__salary = amount
# p = Person("Aviroop", 22)

# print(p.name)          # accessible
# print(p._hobby)        # accessible, but should be avoided
# # print(p.__salary)    #  AttributeError
# print(p._Person__salary)  # Name mangling trick (not recommended)

# p.display_info()
# p.update_salary(60000)



#Abstraction: It is a concept in OOP that allows you to define abstract classes and methods.
# Abstract classes are classes that cannot be instantiated and are meant to be subclassed.
# Abstract methods are methods that are declared but contain no implementation.



# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     def drive(self):
#         print("Driving a vehicle")

#     @abstractmethod
#     def start_engine(self):
#         pass    

# class Car(Vehicle):
#     def start_engine(self):
#         print("Starting the car engine")

# def drive_vehicle(vehicle):
#     vehicle.drive()
#     vehicle.start_engine()

# car = Car()
# drive_vehicle(car)



#generator fn:A generator function in Python is a special kind of function that returns an iterator and allows you to iterate over a sequence of values one at a time, lazily, using the yield keyword.


# def square(n):
#     for i in range(n):
# #         yield i**2
# # gen = square(5)
# # print(gen)  # Output: <generator object square at ...>
# # print(list(square(5)))
# # # Output: [0, 1, 4, 9, 16]
# # print(next(gen)) 
# # print(next(gen)) 
# # print(next(gen)) 
# # print(next(gen)) 
# # print(next(gen))  


# # def read_large_file():
# #     with open('s.txt', 'r') as file:
# #         for line in file:
# #             yield line

# # for line in read_large_file():
# #     print(line.strip())




# # Decorators:A decorator is a function that wraps another function to extend or modify its behavior without permanently changing it.

# # def welcome():
# #     return "WELCOME TO MY WORLD"

# # print(welcome())   # Prints the return value
# # wel = welcome
# # del welcome
# # print(wel())       # Also prints the return value

# #closure fn:A closure is a function that remembers variables from its enclosing scope even after that scope has finished executing.
# # It occurs when:
# # A nested function captures and uses variables defined in its outer function.
# # The outer function has returned, but the inner function still remembers the values.


# # def main_welcome(func):
# #     def sub():
# #         print("welcome to python")
# #         func()
# #     return sub  # ✅ Return the function itself, not its result

# # @main_welcome
# # def intro():
# #     print("wow decorator")

# # intro()  # Now this will work correctly



# # def greet_decorator(func):
# #     def wrapper(name):
# #         print("Hello from decorator!")
# #         func(name)
# #     return wrapper

# # @greet_decorator
# # def say_hello(name):
# #     print(f"Hello, {name}!")

# # say_hello("Aviroop")




# import numpy as np

# # Sample dataset
# data = np.array([10, 20, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# print("Data:", data)

# # Mean

# # Median
# print("Median:", np.median(data))

# # Standard Deviation
# print("Standard Deviation:", np.std(data))

# # Variance
# print("Variance:", np.var(data))

# # Minimum and Maximum
# print("Minimum:", np.min(data))
# print("Maximum:", np.max(data))

# # Percentiles
# print("25th Percentile:", np.percentile(data, 25))
# print("50th Percentile (Median):", np.percentile(data, 50))
# print("75th Percentile:", np.percentile(data, 75))




# import pandas as pd

# data=[1,2,3,4,5,6,7,8,9,10]
# series=pd.Series(data)
# print(series)
# import pandas as pd
# data=[10,20,30,40,50,60,70,80,90,100]
# index=['a','b','c','d','e','f','g','h','i','j']
# series=pd.Series(data,index=index)
# print(series)


# import numpy as np
# import pandas as pd  # Missing import added

# data = {
#     'name': ['Aviroop', 'rohan', 'mahi', 'sachin'],
#     'age': [22, 23, 24, 25],
#     'city': ['kolkata', 'delhi', 'mumbai', 'bangalore']
# }

# df = pd.DataFrame(data)
# print(df)
# arr = np.array(df)
# print(arr)


# import numpy as np
# import pandas as pd  # Missing import added


# print(df.head())
# print(df.tail())
# print(df.loc[0])
# print(df.iloc[0])
# print(df.describe())
# print(df.isnull().any(axis=1))

# Fill NaN values in 'Value' column with its mean and convert to int

# print(df.head())



#Data aggregation and grouping

# import pandas as pd
# import numpy as np
# from io import StringIO
# df = pd.read_csv('Online Sales Data.csv')
# grouped_mean=df.groupby('Product Category')['Unit Price'].mean()
# print(grouped_mean)
# grouped_sum = df.groupby(['Product Name', 'Region'])['Total Revenue'].sum()
# print(grouped_sum)
# grouped_agg= df.groupby(['Product Name', 'Region'])['Total Revenue'].agg( ['sum', 'mean','count'] )
# print(grouped_agg)

import pandas as pd
from io import StringIO
# Data = '[{"employee_name":"Aviroop","employee_salary":100000,"employee_age":20,"Title":"Team Lead"}]'
# df = pd.read_json(StringIO(Data))
# print(df)
# print(df.to_json(orient='records'))



# df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data')
# print(df.head())
# df.to_csv('wine.csv')


#matplotlib: Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications that use general-purpose GUI toolkits, such as Tkinter, wxPython, Qt, or GTK.
# It is used for data visualization and creating static, animated, and interactive visualizations in Python.


# import matplotlib.pyplot as plt
# x=[1, 2, 3, 4, 5]
# y=[10, 20, 25, 30, 40]
# print(plt.plot(x, y))
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# plt.plot(x, y,color='blue', marker='o', linestyle='--', linewidth=1, markersize=3)   # Customize line color, marker, and style
# plt.title("Simple Line Plot")
# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Label")
# plt.grid(True)  # Add grid lines for better readability
# plt.show()  # This opens the plot window




# # Sample data
# x = [1, 2, 3, 4, 5]
# y1 = [i**2 for i in x]
# y2 = [i**0.5 for i in x]
# y3 = [i*2 for i in x]
# y4 = [10, 8, 6, 4, 2]

# # Create a 2x2 grid of plots
# plt.figure(figsize=(10, 8))

# # Plot 1
# plt.subplot(2, 2, 1)
# plt.plot(x, y1)
# plt.title("Square")

# # Plot 2
# plt.subplot(2, 2, 2)
# plt.plot(x, y2, color='green')
# plt.title("Square Root")

# # Plot 3
# plt.subplot(2, 2, 3)
# plt.plot(x, y3, color='red')
# plt.title("Double")

# # Plot 4
# plt.subplot(2, 2, 4)
# plt.plot(x, y4, color='purple')
# plt.title("Descending")

# categories = ['A', 'B', 'C', 'D']
# values1 = [5, 7, 3, 4]
# values2 = [3, 8, 1, 10, 5]
# values3 = [6, 2, 7, 5, 4]
# values4 = [9, 3, 5, 6, 2]

# # Create a 2x2 grid of bar plots
# plt.figure(figsize=(10, 8))

# # Plot 1
# plt.subplot(2, 2, 1)
# plt.bar(categories, values1, color='black')
# plt.title("Plot 1")

# plt.tight_layout()
# plt.show()


# data=[1,2,3,4,5,6,7,8,9,10]
# plt.hist(data, bins=5, color='blue', alpha=0.7, edgecolor='black')
# plt.show()


# scatter plot
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]
# plt.scatter(x, y, color='red', marker='o', s=100)  # s is the size of the marker
# plt.show().


#pie chart
# labels = ['A', 'B', 'C', 'D']
# sizes = [15, 30, 45, 10]
# colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
# explode = (0.1, 0, 0, 0)  # explode the first slice (A)
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)
# plt.show()


# import matplotlib.pyplot as plt
# import pandas as pd
# # sales_data_df=pd.read_csv('Online Sales Data.csv')
# # # sales_data_df.head(5)
# # # total_sales=sales_data_df.groupby('Product Category')['Total Revenue'].sum()
# # # # print(total_sales)
# # # # total_sales.plot(kind='bar', color='blue', alpha=0.7, edgecolor='black')
# # sales_data_df=pd.read_csv('Online Sales Data.csv')
# # sales_trend_df=sales_data_df.groupby('Date')['Total Revenue'].sum().reset_index()
# # plt.plot(sales_trend_df['Date'], sales_trend_df['Total Revenue'], color='blue', marker='o')
# # plt.show()
# import seaborn as sns
# tips = sns.load_dataset('tips')
# # print(tips.head(5))
# sns.kdeplot(tips['total_bill'], shade=True, color='blue')
# plt.show()  
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load example dataset
# tips = sns.load_dataset("tips")

# # Set the theme
# sns.set_theme(style="whitegrid")

# # 1. Scatter Plot
# plt.figure(figsize=(6, 4))
# sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
# plt.title("Scatter Plot")
# plt.show()

# # 2. Line Plot
# plt.figure(figsize=(6, 4))
# sns.lineplot(data=tips.sort_values("total_bill"), x="total_bill", y="tip")
# plt.title("Line Plot")
# plt.show()

# # 3. Histogram
# plt.figure(figsize=(6, 4))
# sns.histplot(data=tips, x="total_bill", bins=20, kde=True)
# plt.title("Histogram")
# plt.show()

# # 4. Box Plot
# plt.figure(figsize=(6, 4))
# sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
# plt.title("Box Plot")
# plt.show()

# # 5. Violin Plot
# plt.figure(figsize=(6, 4))
# sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
# plt.title("Violin Plot")
# plt.show()

# # 6. Bar Plot
# plt.figure(figsize=(6, 4))
# sns.barplot(data=tips, x="day", y="total_bill", estimator=sum, ci=None)
# plt.title("Bar Plot (Sum)")
# plt.show()

# # 7. Count Plot
# plt.figure(figsize=(6, 4))
# sns.countplot(data=tips, x="day", hue="sex")
# plt.title("Count Plot")
# plt.show()

# # 8. KDE Plot (Density)
# plt.figure(figsize=(6, 4))
# sns.kdeplot(data=tips, x="total_bill", fill=True)
# plt.title("KDE Plot")
# # plt.show()

# # # 9. Heatmap (Correlation Matrix)
# # plt.figure(figsize=(6, 4))
# # corr = tips.corr(numeric_only=True)
# # sns.heatmap(corr, annot=True, cmap="coolwarm")
# # plt.title("Heatmap - Correlation Matrix")
# # plt.show()

# # # 10. Pair Plot
# # sns.pairplot(tips, hue="sex")
# # plt.suptitle("Pair Plot", y=1.02)
# # plt.show()

# # # 11. Strip Plot
# # plt.figure(figsize=(6, 4))
# # sns.stripplot(data=tips, x="day", y="total_bill", jitter=True, hue="sex", dodge=True)
# # plt.title("Strip Plot")
# # plt.show()

# # # 12. Swarm Plot
# # plt.figure(figsize=(6, 4))
# # sns.swarmplot(data=tips, x="day", y="total_bill", hue="sex")
# # plt.title("Swarm Plot")
# # plt.show()


# #SQLlite: SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured SQL database engine. It is the most used database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day.
# # It is a serverless, self-contained, zero-configuration, and transactional SQL database engine. SQLite is not a standalone app but a library that software developers embed in their applications.
# import sqlite3

# connection = sqlite3.connect('example.db')
# cursor = connection.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# # Clear table to avoid duplicates
# cursor.execute("DELETE FROM users")

# # Insert fresh users
# users = [("Aviroop",), ("Alice",), ("Bob",), ("Charlie",), ("Diana",), ("Elon",)]
# cursor.executemany("INSERT INTO users (name) VALUES (?)", users)

# connection.commit()

# # Update Aviroop to Aviroop Ghosh
# cursor.execute('''
#     UPDATE users
#     SET name='Aviroop Ghosh'
#     WHERE name='Aviroop'
# ''')
# connection.commit()

# # Fetch and print users
# cursor.execute("SELECT * FROM users")
# all_users = cursor.fetchall()
# for user in all_users:
#     print(f"ID: {user[0]}, Name: {user[1]}")

# connection.close()




# import logging

# # # Configure logging
# logging.basicConfig(
#     filename='app.log',
#     filemode='w',  
#     format='%(asctime)s -  %(name)s - %(levelname)s - %(message)s',  
#     level=logging.DEBUG,
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")



# #logging with multiple loggers
# import logging

# logger1 = logging.getLogger('module1')
# logger1.setLevel(logging.DEBUG)

# logger2 = logging.getLogger('module2')
# logger2.setLevel(logging.WARNING)

# logging.basicConfig(

#     format='%(asctime)s -  %(name)s - %(levelname)s - %(message)s',  
#     level=logging.DEBUG,
#     datefmt='%Y-%m-%d %H:%M:%S'
# )

# logger1.debug("This is a debug message from module1")
# logger2.info("This is an info message from module1")
# logger2.warning("This is a warning message from module1")


import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s -  %(name)s - %(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[  # <-- Missing comma was added here
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmeticApp')

def add(a, b):
    logger.debug(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    logger.debug(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    logger.debug(f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):
    if b == 0:
        logger.error("Division by zero error")
        return "Cannot divide by zero"
    logger.debug(f"Dividing {a} by {b}")
    return a / b

# Running and logging the operations
add_result = add(5, 3)
subtract_result = subtract(5, 3)
multiply_result = multiply(5, 3)
divide_result = divide(5, 3)

print(f"Addition: {add_result}")
print(f"Subtraction: {subtract_result}")
print(f"Multiplication: {multiply_result}")
print(f"Division: {divide_result}")
