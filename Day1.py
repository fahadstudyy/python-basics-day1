#First Day of Python

#Simple Print

print('Hello, Day 1 of python')

#Print by varibales

data = 'This line is stored in a varibale'
print(data)


#arthematic operations

x = 10
y = 20
a = y + x
print(a)

x = 10
y = 20
b = y - x
print(b)

x = 10
y = 20
c = y / x
print(c)

x = 10
y = 20
d = y * x
print(d)

#CHECK TYPE OF VARIABLE

print(type(d))
print(type(c))

#RELATIONAL

x = 30
y = 20
z = y == x
print(z)

#LOGICAL

x = 30
y = 10
z = x > y
print(z)   #It will return either true or false

#INPUT FROM USER

Q1 = input('what is your name?')
print(Q1)

maths = int(input("Enter your marks in math: "))
computer = int(input('Enter your marks in computer: '))
total = maths + computer
print('Total marks: ', total)

#Simple if
x = 10
if x > 10:
    print('This is inside the loob')
print('This is outside the loop')

#if else

x = 15
if x > 15:
    print('x > 15 is true')
else:
    print('x > 15 is not true')

#if else if

x = 15
if x > 15:
    print('x > 15 is true')
elif x < 15:
    print('x < 15 is true')
else:
    print('all of them are false')

# Loops
#while loop
i = 1
while i<10:
    print(i)
    i = i + 1
#for loop
for i in range (0,10):
    print(i)

#for loop with 2 incriment
for i in range (0,10,2):
    print(i)

# A few more arithmetic examples
b = x * y
print(b)
