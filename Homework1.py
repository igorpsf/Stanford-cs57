#1)
from pip._vendor.distlib.compat import raw_input

print((True and False) and True) or (True and False) or (True or True)     # True
# False and True or False or True
# False or True
# True

#2)
a = 'catsanddogs'
print(a[3:9]) # sanddo
print(a[2:])  # tsanddogs
print(a[-3])  # o

#3)
word = (raw_input('Enter a word: '))
print('Lenght of the word: ', len(word))
# or
#print 'Lenght of the word: ' + str(len(word))

#4)
number = (int(raw_input('Enter a number: ')))
print(number ** 3)
# or
#print number * number * number

#5)
radius = (float(raw_input('Enter a radius: ')))
pi = 3.14159
area = (pi * radius * radius)
print(area)


