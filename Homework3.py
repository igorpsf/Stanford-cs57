# 1) Write a function maxVal(x,y,z) that takes in three numbers and returns whichever is highest.

def maxVal(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z

print(maxVal(1,2,3))     # 3
print(maxVal(2,3,1))     # 3
print(maxVal(3,1,2))     # 3

# or

def maxVal(x, y, z):
    return max(x,y,z)
print(maxVal(5,2,3))     # 5


# 2) Write a function longStr(str1,str2) that takes in two strings and returns whichever string is longer.

def longStr(str1,str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    elif len(str1) == len(str2):
        print("Len's are equal")

print(longStr('Hello', "Hi"))    # Hello
print(longStr('Hi', "Hello"))    # Hello
longStr('Hi', "Hi")             # Len's are equal

# 3) Write a function vowelCheck(char) that takes a character as input and determines if the input is a vowel. For ex: vowelCheck('a') -> True; vowelCheck('c') -> False

def vowelCheck(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels:
        return True
    else:
        return False

print(vowelCheck('a'))   # True
print(vowelCheck('c'))   # False

# 4) Write a function revStr(str) that takes in a string and returns the string in reverse order.

def revStr(str):
    return str[::-1]

print(revStr('Hello'))   # olleH

def revStr2(str):
    rev = ''
    for i in str:
        rev = i + rev
    return rev

print(revStr2('Hello'))  # olleH