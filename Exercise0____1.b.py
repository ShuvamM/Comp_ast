#Exercise1____1.b.py




#################################################
#################################################
#################       incomplete       ########
#################################################
#################################################





#################################################
#################################################
#################       i       #################
#################################################
#################################################
"""
Declare a list L = [10, -3, 0.5, "eleven"].
i. Print the length of the list on the screen in the format: "The list has <this many> elements."
"""

L = [10, -3, 0.5, "eleven"]
print('The list has ' +str(len(L)) + ' elements')
print('')

#################################################
#################################################
#################      ii       #################
#################################################
#################################################
"""
ii. Loop through the list and print the type of each element in the format:
"<element> is of type <type of that element>".
"""

for i in range(0,len(L)):
    print('element ' +str(i+1) +(' = ') +str(L[i]) +' is of type ' +(str(type(L[i]))))

print('')

#################################################
#################################################
#################      iii      #################
#################################################
#################################################
"""
iii. Write a function that finds the minimum of all numbers in that list. The function should check each
element to make sure it’s a number, and exclude it if it isn’t (hint: check their type!).
Redefine L = [10, -3, 0.5].
"""

def Min(L):
    L2 = []
    for i in range(0,len(L)):
        try:
            if float(L[i])==int(L[i]) or float(L[i])==float(L[i]):
                L2.append(L[i])
        except ValueError:
            pass
    for i in range(1,len(L2)):
        if L2[i]<L2[i-1]:
            L2_min = L2[i]
        else:
            L2_min = L2[i-1]
        
    return L2,L2_min

            
Min = Min(L)
print('Redefined L  = ' +str(Min[0]))
print('Minimum of L = ' +str(Min[1]))


#################################################
#################################################
#################      iv       #################
#################################################
#################################################
"""
iv. Write a function that loops through a list of numbers by index and adds 1 to each element, returning
nothing.
"""

def plus(L):
    L2 = []
    for i in range(0,len(L)):
        try:
            if float(L[i])==int(L[i]) or float(L[i])==float(L[i]):
                L2.append(L[i])
        except ValueError:
            pass
    
    for i in range(0,len(L)):
        try:
            if float(L[i])==int(L[i]) or float(L[i])==float(L[i]):
                L2.append(L[i]+1)
        except ValueError:
            pass

#################################################
#################################################
#################      v        #################
#################################################
#################################################
"""
v. Write a function that accepts a list of numbers and returns a new list that contains each element of
the input incremented by 1 (e.g., add_one_to(L) → [11, -2, 1.5]). Hint: You can use append, list
comprehensions, or even the copy module for this.
"""

def add_one_to(L):
    L2 = []
    for i in range(0,len(L)):
        try:
            if float(L[i])==int(L[i]) or float(L[i])==float(L[i]):
                L2.append(L[i])
        except ValueError:
            pass
    
    for i in range(0,len(L)):
        try:
            if float(L[i])==int(L[i]) or float(L[i])==float(L[i]):
                L2.append(L[i]+1)
        except ValueError:
            pass
        return L2













#################################################
#################################################
#################      vi       #################
#################################################
#################################################
"""
vi. Apply the functions you wrote in (iv) and (v) to the list L, printing the contents of L before and after
each function is called. Can you explain what happened?
"""
print('')
print('L = ' +str(L))
plus_L = plus(L)
print('plus_L = ' +str(plus_L))


add_one_to_L = add_one_to(L)
print('add_one_to_L = ' +str(add_one_to_L))













































