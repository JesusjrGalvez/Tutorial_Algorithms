# Permutations recursively
# Tutorial from Algorithms in Python – Full Course for Beginners
# https://youtu.be/fW_OS3LGB9Q?t=900

import time


def permutation_recursive(str_, pocket):
    if len(str_) == 0:
        print("HI")
        print(pocket)
    else:
        for i in range(len(str_)):
            letter = str_[i]
            front = str_[0:i]
            back = str_[i + 1:]
            together = front + back
            permutation_recursive(together, letter + pocket)


from math import factorial


def permutation_iterative(str_):
    for p in range(factorial(len(str_))):
        print(''.join(str_))
        i = len(str_) - 1
        while i > 0 and str_[i - 1] > str_[i]:
            i -= 1
        str_[i:] = reversed(str_[i:])
        if i > 0:
            q = i
            while str_[i - 1] > str_[q]:
                q += 1
            tem = str_[i - 1]
            str_[i - 1] = str_[q]
            str_[q] = tem


print(permutation_recursive("AB", ""))
print(permutation_iterative(list("ABZ")))
