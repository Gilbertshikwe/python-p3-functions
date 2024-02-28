#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()
def greet(name="Naureen"):
    print(f"Hello, {name}!")
greet()

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    return num1 + num2
result = add(45,55)
print(result)

def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2

# Examples
result1 = halve(4)
print(result1)  # Output: 2.0

result2 = halve("two")
print(result2)  # Output: None

