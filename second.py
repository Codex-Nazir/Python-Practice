import re 
import csv
import json
import pandas as pd

#this is a string with multiple lines.
text = "The rain is Spain"
match = re.search(r"rain", text)

if match:
    print("Match found :", match.group())
else:
    print("Match not found :")

matches = re.findall(r"ain", text)
print("Match found :", matches)

#This is a string with multiple lines.
new_text = re.sub(r"ain", "sun", text)
print("Replaced text :", new_text)

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

file1 = open('example_new.txt', 'w')
file1.write("This is a new text file.\n It contain important things.")
file1.close()

with open('example.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

with open('example_new.txt', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Age", "City"])
    csv_writer.writerow(["Nazir", 23, "Jammu"])
    csv_writer.writerow(["John", 30, "New York"])
    csv_writer.writerow(["Alice", 25, "Los Angeles"])
    csv_writer.writerow(["Bob", 28, "Chicago"])

# dictionary to json
data = {
    "Name" : "Nazir",
    "Age" : 23,
    "City" : "Jammu"
}

with open('example.json', 'w') as file:
    json.dump(data, file, indent = 4)

with open('example.json', 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent = 4))

for key, value in data.items():
    print(f"{key}: {value}")

pi = 3.141592653589793
formatted_pi = "Pi rounded to 2 decimal is {:.2f}.".format(pi)

number = 42
padded_num = "The number is {:05d}.".format(number)


original_string = "Hello, World!"
uppercase_string = original_string.upper()

lowercase_string = original_string.lower()

sentence = "Python is a powerfull Language"
words = sentence.split()

fruits = ["apple" , "Banana" , "Cherry"]

my_tuple = {1,2,3,4,5}
packed_tuple = ("apple","banana","cherry")
(fruit1, fruit2, fruit3) = packed_tuple

my_dict = {
    "name" : "Nazir",
    "age"  : 23,
    "city" : "jammu"
}

my_tuple_b = {3,4,5,6,7,1}
union_set = my_tuple.union(my_tuple_b)
intersection_set = my_tuple.intersection(my_tuple_b)
difference_set = my_tuple.difference(my_tuple_b)

print("first fruit : ",fruits[0])
print("Second fruit : ",fruits[1])
print("Third fruit : ",fruits[2])

fruits[1] = "blueberry"
print("Modified List :", fruits)

fruits.append("orange")
print("Lsit after adding an element :", fruits)

fruits.remove("apple")
print("List after removing : ", fruits)

fruits.insert(1,"blueberry")
print("after insert : ", fruits)

popped_fruit = fruits.pop(2)
print("after pop : ", fruits)
print("popped fruit : ", popped_fruit)

index_of_orange = fruits.index("orange")
print("Index of Orange :", index_of_orange)

print("The entire tuple :", my_tuple)

print("First element :", [0])
print("Last element :", [-1])

print("Fruit 1 :", fruit1)
print("Fruit 2 :", fruit2)
print("Fruit 3 :", fruit3)

print("Original dictionary :", my_dict)

my_dict["email"] = "nazir@gmail.com"
print("after modifying email :", my_dict)

my_dict["age"] = 20
print("After modifying age :", my_dict)


print("Union of my_tuple and my_tuple_b is :", union_set)
print("Intersection of my_tupple and my_tuple_b is :", intersection_set)
print("Diference is :", difference_set)

print("Uppercase :", uppercase_string)
print("Lowercase :", lowercase_string)

print("Split into words :", words)


print(formatted_pi)

print(padded_num)

# try and except block
try:
    number = int(input("Enter a number: "))
    result = 10/number
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
finally:
    print("Execution completed.")

try:
    file = open('example1.txt', 'r')
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")

# making class
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print("Caught Custom Error:", e)


def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

try:
    result = divide(10, 1)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)

#for practice insta question 
print(len({1,1,2,2,3}))

# dictionary
data = {
    "Name" : ["Nazir", "John", "Alice", "Bob"],
    "Age" : [23, 30, 25, 35],
    "City" : ["Jammu", "New York", "London", "Paris"]
}

df = pd.DataFrame(data)
print(df)
# to make in a excel file

df.to_excel("example.xlsx", index=False)

print(pd.__version__)

#This is matplotlib example
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Line Graph") 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#This is Math lib example
import math

x = 16
sqrt_x = math.sqrt(x)
print("Square root of", x, "is", sqrt_x)

n = 5
factorial_n = math.factorial(n)
print("Factorial of", n, "is", factorial_n)

# This is Date and time example
import datetime

current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

#This is custom date example
custom_date = datetime.date(2023, 4, 15)
print("Custom date:", custom_date)
