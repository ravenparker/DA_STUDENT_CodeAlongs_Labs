#!/usr/bin/env python3
"""Day 4 code-along: Local vs. Global Variables & Scope. Run: python3 <file>"""

# ===== 1. Local Scope, Live =====
# Find out if a variable made inside a function exists outside it.
# TODO: run it, read the NameError, then comment out the raising line
# DISCUSS: Order: A: total disappears. B: make_total() runs. C: total = 100.
# Your answer:
#
print('----- 1. Local Scope, Live -----')
# TODO: define make_total() with a local variable total set
# to 100, returning it, then try printing total outside the
# function and watch what happens
def make_total():
    total = 100
    print(total)
    return total

# print(total)
make_total()

# DISCUSS: set_x() sets x = 5, but print(x) outside raises NameError. Why?
# Your answer:
# `x`` is a local variable within set_x(), meaning it's contained within the function.
# Since it is limited to the function, a NameError is received because it's not defined elsewhere.


# ===== 2. Reading a Global, Live =====
# Price a $100 item with 8% tax, using a tax rate stored outside the function.
print('----- 2. Reading a Global, Live -----')
# TODO: define tax_rate as a global
# TODO: write price_with_tax(price) that reads tax_rate directly

# DISCUSS: Move price_with_tax to a file with no tax_rate. Why does it break?
# Your answer:
#
#

tax_rate = .08
def price_with_tax(price): 
    price = price + (price * tax_rate)
    return price

price_with_tax(100)

# ===== 3. Refactor: Global to Parameter =====
# Pass the tax rate in as a parameter. It should still print 108.0.
print('----- 3. Refactor: Global to Parameter -----')
# TODO: rewrite price_with_tax to take tax_rate as a parameter
tax_rate = 0.08
