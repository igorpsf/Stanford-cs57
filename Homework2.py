# 1) Write the below programs with a while loop and a for loop:

# a) Sum the even numbers from 0 to 100 (inclusive)

# while
from pip._vendor.distlib.compat import raw_input

number1 = 0
total1 = 0
while number1 < 100:
    number1 += 2
    total1 += number1
print('Sum the even numbers from 0 to 100 (inclusive):', total1)

# for loop
number2 = 0
for number in range(0, 101, 2):
    number2 += number
print('Sum the even numbers from 0 to 100 (inclusive): ' + str(number2))

# Sum the odd numbers from 0 to 100 (inclusive)

# while
number3 = 1
total3 = 1
while number3 < 99:
    number3 += 2
    total3 += number3
print('Sum the odd numbers from 0 to 100 (inclusive): ', total3)

# for loop
number4 = 0
for number in range(1, 100, 2):
    number4 += number
print('Sum the odd numbers from 0 to 100 (inclusive): ', number4)

#or
###**********************************************************
c1 = 0
for i in range(0, 101):
    if i % 2 == 0:
        c1 += i
print('Sum the even numbers from 0 to 100 (inclusive):', c1)

c2 = 0
for j in range(0, 101):
    if j % 2 != 0:
        c2 += j
print('Sum the odd numbers from 0 to 100 (inclusive): ', c2)
###***********************************************************


# 2) "Write a program that counts the vowels in this sentence."
message = "Write a program that counts the vowels in this sentence."
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for vowel in message:
    #if vowel == 'a' or vowel == 'e'or vowel == 'i' or vowel == 'o' or vowel == 'u':
     if vowel in vowels:
        count += 1
print(count)


# 3) Asks a user to enter a temperature in celsius (via raw_input) and outputs the temperature in fahrenheit.

temperature = (int(raw_input("Enter a temperature in celsius: ")))
fahrenheit = (temperature * 9/(5 * 1.0)) + 32
#fahrenheit = (temperature * 9/float(5)) + 32
print('Temperature in fahrenheit: ', fahrenheit)


# 4) Write a program that outputs the value of adding all numbers 1 to n.
# A user will input n via raw_input. Assume n is a positive integer greater than 1.
# For Example: n of 4, would result in 10 (1+2+3+4)
n = (int(raw_input('Enter a number: ')))

result = 0
for i in range(n + 1):
    result += i
print(result)

#or

#result2 = 0
#c = 0
#while result2 < n:
#    c += 1
#    result2 += c
#print result2