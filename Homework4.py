# 1) Explain the differences between print and return.
# Include a few examples highlighting that you understand the differences.


# If don'r define return in function, then by default function will return 'None'

def f(x):
    print(x + 1) # 3
f(2)            # 3
y = f(2)        # y = None (saving return function, but it is None by default.)
print('y:', y)   # None

def g(x):
    return x + 1
g(2)
x = g(2)        # x = 3
print('x:', x)


# 2) Take a look at recur(x) from this slide.
# Verbally (in short paragraph form) explain to me what happens when I execute recur(-5), recur(0), recur(5).

def recur(x):
    if x == 1:
        print("In the if statement, x is " + str(x))
        return x
    else:
        print("In the else statement, x is " + str(x))
        return recur(x-1)

#recur(-5)   # Infinite loop
#recur(0)    # Infinite loop
recur(5)    # Will execute else condition until if branch will be True (x equal 1)




# 3) Write a function iterFact(5) using iteration that takes 1 number as inputs and computes the factorial calculation.
# Assume positive numbers. Ex: iterFact(5) -> 120

def iterFact(a):
    sum = 1
    while a >= 1:
        sum = sum * a
        a -= 1
    return sum

print (iterFact(5))   # 120

# or

def iterFact(x):
    count = 1
    total = 1
    while count <= x:
        total = total * count
        count += 1
    return total


# 4) Write a function iterPower(4,3) using iteration that takes two positive number (x,y) as inputs and computes x^y.
# Assume positive numbers. Ex: iterPower(4,3) -> 64

def iterPower(a,b):
    sum = 1
    while b > 0:
        sum *= a
        b -= 1
    return sum

print (iterPower(4,3))    # 64
print ('check', 4**3)     # 64
# 4**3 == 4 * 4 * 4

# 5) Write a function numOrder(a,b,c,d) that takes in four non-sequential numbers and returns them in sequence.

def numOrder(a,b,c,d):
    list = [a,b,c,d]
    list.sort()
    return list

print (numOrder(4,1,3,2))     # [1, 2, 3, 4]

# or

def numOrder2(a,b,c,d):
    l = [a,b,c,d]
    i = 0
    while i < 3:
        if l[i] <= l[i+1]:
            i += 1
        elif l[i] > l[i+1]:
            tmp = l[i]
            l[i] = l[i + 1]
            l[i+1] = tmp
            i=0
    return l

print (numOrder2(1,3,4,2))

# or

def numOrder3(a,b,c,d):
    if a <= b and b<=c and c<=d:
        return [a,b,c,d]    # return order list if no changes needed
    elif a > b:
        return numOrder3(b,a,c,d)   # Flip a and b
    elif b > c:
        return numOrder3(a,c,b,d)   # Flip b and c
    elif c > d:
        return numOrder3(a,b,d,c)   # Flip c and d

print (numOrder3(1,4,3,2))
