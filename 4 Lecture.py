def pvsr(x):
    print(4)
    print(3)
    print(2)
    return x

print (pvsr(1))
y = pvsr(1) # store only return (1)
print(y)

list = [14, 24, 14, 230, 100]

def fun(list):
    i = 0;
    while i < len(list):
        list[i] = (list[i] + 10) // 2   # Python 3 // for division and see integers, instead of floats
        i += 1
    return list

print(fun(list))


def f(x):
    print (x + 1)
f(2)
y = f(2)    # y = None
print(y)     # None

def g(x):
    print (x + 1)
g(2)
x = g(2)    # x = 3
print(x)


def h(a,b,c):
    x = a + b       # 3
    return i(x,c)   # 3,3

def i(a,b):
    c = a + b       # 6
    return c        # 6

print(h(1,2,3))


def newFunc(a):
    oldFunc(a)      # None
def oldFunc(b):
    b = b - 1
    return
print(newFunc(3))


################## Recursion

def count(n):
    if n > 0:
        print (n)
        return count(n-1)
    else:
        print ("Blastoff!")
        return
count(3)

def recur(x):
    if x == 1:
        print ("In the if statement, x is " + str(x))
        return x
    else:
        print ("In the else statement, x is " + str(x))
        return recur(x-1)

print(recur(3))



# Iterative
#5 = 5 + 5 + 5

# Recursive
#5 * 3 = 5 + (5 * 2)
#5 * 2 = 5 + (5 * 1)
#5 * 1 = 5

# iteration
def iterMult(a,b):
    sum = 0
    while b > 0:
        sum = sum + a
        b -= 1
    return sum
print(iterMult(4,3))     # 12

# Recursive

def revMult(x,y):
    if y == 1:
        return x
    else:
        return x + revMult(x, y - 1)

print(revMult(2,3))

#rm(2,3) -> 2 + rm(2,2) -> 2 + rm(2,1) -> 2     # 6