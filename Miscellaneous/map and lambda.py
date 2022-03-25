"""map() function returns a map object
of the results after applying the given iterable """

# python program to demostrate working #
def addition(n):
    return n + n


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Using of the lamda expression
"""syntax of lambda expression:
lambda arguments : expression"""

numbers = (1, 2, 3, 4)
result = map(lambda x: x+x, numbers)
print(list(result))


#add two list
number1 = [1, 2, 3]
number2 = [4, 5, 6]

result = map(lambda x, y: x+y, number1, number2)
print(list(result))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a+b+c
print(x(5, 6, 2))

def fun(n):
    return lambda a: a*n

def fun1(n):
    return lambda a: a*n

