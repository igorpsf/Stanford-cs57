list = ["Washington", "Adams", "Jefferson", "Madison", "Monroe"]

def re(list):
    return list[::-1]

print(re(list))

list2 = [14, 23, 14, 230, 100]
def listmatch(li):

    for i in range(len(li)):
        li[i] = (li[i]+10)/2
    return li

print(listmatch(list2))

state = "Mississippi"
countMP = 0
countIS = 0

for char in state:
    if char == "M" or char == "p":
        countMP += 1
    elif char == "i" or char == "s":
        countIS += 1

print("The count of M & P's are:", countMP)
print("The count of I & S's are:", countIS)


string = "Hello"

def char(string):
    for ch in string:
        print(ch)
char(string)

h = 'stanford'
print(h.islower())  # True

a = "cats are the best!"
print(a.replace("cats", "dogs"))    # dogs are the best!

d = "disneyland"
print(d.capitalize())   # Disneyland


for n in range(51):
    if (n == 0 or n == 1):  # Handles case for n == 0 or n == 1
        continue
    if (n == 2):    # Handles case for n == 2
        print(str(n) + " is prime")
    for i in range(2, n):
        if (n % i == 0):  # If n%i == 0 then we know n cannot be prime. Ex: 4%2, 8%2.
            break
        if (i == n - 1):  # This means we have evaluated every possible divisor besides n.
            print(str(n) + " is prime.")


