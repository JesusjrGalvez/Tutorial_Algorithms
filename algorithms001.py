# Tutorial from Algorithms in Python – Full Course for Beginners
# https://www.youtube.com/watch?v=fW_OS3LGB9Q
import time


def factorial_iterative(n):
    sol = 1
    for i in range(1, n+1):
        sol *= i
    return sol


# Watch:
# https://www.programiz.com/python-programming/recursion
# Recursion needs a BASE CONDITION to exit the recursion.
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return factorial_recursive(n-1) * n


st = time.time()
print(factorial_iterative(900))
et = time.time()
print(et-st)

st = time.time()
print(factorial_recursive(900))
et = time.time()
print(et-st)
