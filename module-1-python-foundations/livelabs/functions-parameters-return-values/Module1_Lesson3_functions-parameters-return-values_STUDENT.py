#!/usr/bin/env python3
"""Day 3 code-along: Functions, Parameters & Return.... Run: python3 <file>"""

# ===== 1. Define and Call, Live =====
# Build a reusable greeting: one function, called twice, prints it twice.
print('----- 1. Define and Call, Live -----')
# TODO: define a function named greet that prints a welcome
# message, then call it twice
def greet():
    print("Hello")

greet()
greet()

# ===== 2. Parameters, Live =====
# Make greet work for anyone: pass in a name, then greet Jordan and Amara.
print('----- 2. Parameters, Live -----')
# TODO: add a name parameter to greet, and print a
# personalized welcome message for each of 2 names
def greet(username):
    print("Hello, ", username)

greet("Jordan")
greet("Amara")

# DISCUSS: Order double(5): A: n becomes 5. B: body runs. C: it gets called.
# Your answer:
# A: n becomes 5
#
#
# PREDICT before you run: Given def double(n): print(n * 2), what does
#                         double(5) print?
# Your answer:
# 10
#


# ===== 3. Return, Live =====
# Send a value back with return to use it in math. double(5) + 1 prints 11.
print('----- 3. Return, Live -----')
# TODO: write double(n) using return (not print), then use
# its result in an expression - add 1 to it and print that
def double(n):
    return(n * 2)

result = double(7) + 1
print(result)

# DISCUSS: A doubling function's result + 1 raises TypeError. Likely cause?
# Your answer:
# A function that returns a TypeError when adding 1 likely only prints the result and doesn't return it.
# 
