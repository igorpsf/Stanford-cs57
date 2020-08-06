# from pip._vendor.distlib.compat import raw_input

x = 5       # int
a = 10.1    # float
b = False   # bool
c = 'dog'   # str
c1 = 'dog\'s'
c2 = """ Bobby's
car"dddd """
d = (1,2)   # Tuple, immutable data type

print(type(x))
print(type(a))
print(type(b))
print(type(c))

print(1 + 1.0)               # 2.0
print(3/2)                   # 1
print(2 * 3.5)               # 7.0
print(float(3)/float(2))     # 1.5
print(int(3)/int(2))         # 1

print(not True)              # False
print(True and True)         # True, any other False
print(False and True)        # False

print(True or False)         # True, either one side is True
                              # different boolean operators

print(True == 1)             # True
print(False == 0)            # True


d = 'dog'
d = 6
print(d)

a = 'Losangeles'
print(a.lower())    # losangeles
print(a.upper())    # LOSANGELES
print(a.count("Los"))    # 1
print(a.count("e"))      # 2
print(a.find("e"))      # 6 - return index where is e
print(a.find("w"))      # -1 - because w is not in our string

message = "Hello World"
m = message.replace("World", "Universe")
print(message)
print(m)

greeting = "Hello"
name = "Michael"
message = greeting + ", " + name + ". Welcome!"

message2 = "{}, {}. Welcome!".format(greeting, name) # place holders
message3 = f"{greeting}, {name.upper()}. Welcome!"  # Only for Python 3.6 and newer


print(message)
print(message2)
print(message3)

print(dir(name))        # show all attributes and methods
print(help(str))        # help about str




print(len(a))        # 10
print(a[0])          # l
print(a[-1])         # s
print(a[-10])        # l

print(a[1:3])        # os

#name = raw_input("My name is: ")
#print("Your name is", name)
