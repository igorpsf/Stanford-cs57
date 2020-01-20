# 1) Using recursion, calculate n! for any integer >=0.
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(5))      # 120

# 2) Using recursion, calculate x^y for any integers x,y >=0.

def power(x,y):
    if y==0:
        return 1
    elif y >= 1:
        return x * power(x, y-1)

print(power(4,3))        # 64

# 3) Given a list of any size, re-order the list such that it is in sequence.
# Assume input is a list of any length (positive integers), function returns ordered list.

l = [5,1,3,4,2,7,6,10,9,8]

print(len(l))
def sort(l):
    i = 0
    while i < len(l)-1:
        if l[i] <= l[i + 1]:
            i += 1
        elif l[i] > l[i + 1]:
            tmp = l[i]
            l[i] = l[i + 1]
            l[i + 1] = tmp
            i = 0
    return l

print(sort(l))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
