#dealing with errors in python
# syntax error or exceptions
# syntatical error occurs when the syntax is not correct
# exception: the syntax is correct but it throws an error:

#for example:

list1 = [34, 2, 52, 63]
#
# print(list1[3])
# print(list1[4]) # u will see the index error here: out of range

#let's now use try and except a bit
#Index error
try:
    print(list1[3])
    print(list1[4])
except IndexError:
    print('Error detected')

#divisionerror nameerror
try:
    a = 4
    if a < 5:
        print(a/(4-a))
except (ZeroDivisionError, NameError):
    print('Error occured and handled')

# using else method

b = 4
try:
    if b > 3:
        c = (b + 3)/(5 - b)
except ZeroDivisionError:
    print('OOps! Error has been handled after detection')
else:
    print(c)

# Python program to demonstrate finally

# No exception Exception raised in try block
try:
    k = 5 // 0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

def divide():
    x = float(input('first no: '))
    y = float(input('second no: '))
    try:
        result = x / y
    except ZeroDivisionError:
        return 'You can\'t divide a number with zero'
    else:
        return result
print(divide())





