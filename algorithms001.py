# Tutorial from Algorithms in Python – Full Course for Beginners
# https://www.youtube.com/watch?v=fW_OS3LGB9Q

def factorial_iterative(n):
    sol = 1
    for i in range(1, n+1):
        sol *= i
    return sol


# Watch:
# https://www.programiz.com/python-programming/recursion
def factorial_recursive(n):
     if n == 1:
         return n
     else:
         #tem = factorial_recursive(n-1)
         #tem = tem * n
        return factorial_recursive(n-1) * n

#
# factorial(3)  # 1st call with 3
# 3 * factorial(2)  # 2nd call with 2
# 3 * 2 * factorial(1)  # 3rd call with 1
# 3 * 2 * 1  # return from 3rd call as number=1
# 3 * 2  # return from 2nd call
# 6  # return from 1st call


print(factorial_iterative(5))
print(factorial_recursive(3))