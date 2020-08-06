# Print vs Return
def printmaster(x):
    print(4)
    print(3)
    print(2)
    print(1)

# Example 1 with print
printmaster(1)          # 4,3,2,1
print(printmaster(1))   # 4,3,2,1, None
y = printmaster(1)      # 4,3,2,1
print(y)                # None
print(type(y))          # type "NoneType"

# Example 2 with return
def retmaster(x):
    return 4
    return 3
    return 2
    return 1
retmaster(1)            # blank
print(retmaster(1))     # 4, function execute only first return
y = retmaster(1)        # blank
print(y)                # 4
print(type(y))          # "class int"


# Function input/outputs
def batman(var1):
    return (var1)
print(batman("bob"))    # bob

def batman (var1, var2, var3):
    return (var1, var2, var3)

print(batman(1,2,3))    # (1,2,3) - tuple

def batman (var1, var2, var3):
    return [var1, var2, var3]

print(batman(1,2,3))    # [1,2,3] - list


# Assertions and Exceptions

def divide(x,y):
    x = float(x)
    y = float(y)
    result = x/y
    return result

def divideNew(a,b):
    try:
        a = float(a)
        b = float(b)
        result = a/b
    except ZeroDivisionError as error:
        print('Cannot divide by zero! ', error)
    else:
        print('The result is', result)

divideNew(4,0)

# def divideAssert(x,y):
#     assert y != 0, "Hey Stanford! You can't divide by 0!"
#     x = float(x)
#     y = float(y)
#     result = x / y
#     return result
#
# print (divideAssert(3,0))

def divideTry(x,y):
    try:
        assert y != 0, "You can't divide by 0!"
        x = float(x)
        y = float(y)
        result = x / y
        return result
    except AssertionError as error:
        print(error)

divideTry(3,0)



# Dictionaries

groceries = {'Apples': 1.99, 'Bananas': 0.99, 'Cheese': 2.99}
print (groceries)

groceries['Donuts'] = 2.49
groceries['Eggs'] = 1.49
print(groceries)

del groceries['Eggs']
print(groceries)

# Using recursion, find the length of a string.
# Your function should take in a string and output the length. Do not use len().
def findLen(str):
    if str == '':
        return 0
    else:
        str = str[:-1]      # 1) Stanfor,
        return 1 + findLen(str)     # 2)Stanfo ...

print (findLen('Stanford'))

print('str'[:-1])      # st
print('str'[-1])        # r
print('str'[1:-1])        # t



# Fibonacci Number 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,

# Recursion
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(5))       # 5


# Iteration
def iterFibo(n):
    a,b = 0,1
    for i in range(0, n):
        a,b = b, a + b
    return a
print(iterFibo(5))   # 5