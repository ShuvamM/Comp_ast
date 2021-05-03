#Exercise1____1.a.py

#################################################
#################################################
#################       i       #################
#################################################
#################################################
"""
Declare two variables a = 3 and b = 2.0.
i. What is the type of each variable? What is the type of their sum and product?
"""
a = 3
b = 2.0

print('i')
print('type of variable a = ' +str(type(a)))
print('type of variable b = ' +str(type(b)))
print('type of "a + b"    = ' +str(type(a+b)))
print('type of "a * b"    = ' +str(type(a*b)))
print('')

#################################################
#################################################
#################      ii       #################
#################################################
#################################################

"""
ii. Print the values on the screen in the format "The value of a is <value of a> and the value of b is <value
of b>".
"""
print('ii')
print('The value of a is ' +str(a))
print('The value of b is ' +str(b))

#################################################
#################################################
#################      iii      #################
#################################################
#################################################


"""
iii. Let the user input a numeric(integer or float), then print the result of a/c.
value and store it in the variable c (hint: use the command input!). Assert
that the input is really a number 
""" 

print('iii')
c = input("Enter the value of c : " )
if float(c) == int(float(c)):
    print('c is an integer')
    c = int(c)
elif float(c) == float(c):
    print('c is a float')
    c = float(c)
else:
    print('c is neither a float nor an integer')
    
    

#Print a/c
print('a/c = ' +str(a/c))
print('')

#assert type(c) is int, "id is not an integer: %r" % c

#################################################
#################################################
#################      iv       #################
#################################################
#################################################


"""
iv. Write a function that finds and returns the maximum between two numbers. Apply the function between
a and c, then print the result. Try different values for c (or even something that will cause errors!).
"""

print('iv')
def Max(a,b):
    if a>b:
        Max = a
    elif b>a:
        Max = b
    return Max

c = c
print('Maximum of a = 3 and c = ' +str(c) +' is ' +str(Max(a,c)))
c = 4
print('Maximum of a = 3 and c = ' +str(c) +' is ' +str(Max(a,c)))




