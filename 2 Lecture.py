from pip._vendor.distlib.compat import raw_input

# a = [0,1,2,3,4]
# a[0]=8

# print(a[0])     # 8
# print(a[0:2])   # [8, 1]
# print(a[:2])    # [8, 1]
# print(a[2:4])   # [2, 3]

print(list(range(4)))       # [0, 1, 2, 3]
print(list(range(4,8)))     # [4, 5, 6, 7]
print(list(range(1,13,2)))  # [1, 3, 5, 7, 9, 11]

# count = 10
# while (count != 0):
#     print(count)
#     count-=1
# print("Blastoff!")

# for x in [0,1,2,3]:
#     print(x)
#
# print()
# for x in range(4):
#     print(x)


# x = (int(raw_input("What is 2+2?: ")))
# if x == 4:
#     print("Nice work!")
# elif (x ==3) or (x == 5):
#     print("So close!")
# else:
#     print("Try again!")

# in in Strings
print("test" in "testing")  # True
print("boss" in "boston")   # False

# in in Lists
print(3 in [1,2,3])  # True
print("a" in ['a', 'b', 'c'])   # True

studentList = ["Bob", "Charlie", "Jessica", "Sally"]
student = "Allison"
if student in studentList:
    print(student + " is in the calss!")
else:
    print(student + " is NOT in the calss!")


total = 0 #instantiates total variable and assigns value
number = 0 #instantiates number variable and assigns value

while (number < 5): #condition stays true as long as number < 5
    number += 1 #increments number by 1
    total += number #adds number to sum to give updated subtotal value

print("The sum of numbers from 1 to 5 is ", total)

total = 0 #instantiates total variable and assigns value

for number in range(51): #for each number until 50
    total += number #adds number to total to give updated subtotal value

print("The sum of numbers from 1 to 50 is " + str(total))



# score = (int(raw_input('Enter a score: ')))
# if score >= 90 and score <= 100:
#     print ('Score is: A')
# elif score >= 80:
#     print ('Score is: B')
# elif score >= 70:
#     print ('Score is: C')
#
# if 'bos' in 'bols':
#     print (True)
# else:
#     print (False)