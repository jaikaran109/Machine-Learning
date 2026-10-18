# Java Program to Calculate Compound Interest


principle = float(input())
rate = float(input())
n = float(input())
time = float(input())

amount = principle * (1 + (rate / 100) / n) ** (n * time)
compound_interest = amount - principle

print(compound_interest)
