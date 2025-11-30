'''
we know that pyhton is a dynamic programming language
pyhton automaticallly understands the data type

1)Numeric => int, float, complex
2)Boolean => bool (True/False)
3)Strings
4)List (Mostly used to store homogeneous data types)
5)Tuple (Faster comapred to list)
6)set (unordered collection of items)
7)Dictionary (Unordered collection of key-values pairs, keys are uniques and values may not be unique)
'''
a = 3;
b = 4.67
c = 3 + 5j
print(type(a))
print(type(b))
print(type(c))


#Working on float numbers
#assigning large float number 
f = 1.23e3 #1.23 * 10 power 3
print(type(f))

g = 1.78E-35#1.78*10 power -34 AND here e is not a case sensitive
print(g)
print(type(g))


#Working on complex numbers
c = 10 + 20j #real value = 10 and imaginary value = 20 and j =iota
print(c)
print(type(c))
print(c.real)#10.0
print(c.imag)#20.0
print(isinstance(c , complex)) #checking wheather c is complex datatype or not


#working on boolean values
h = True
print(type(h))
print(isinstance(h,bool)) #True
print(isinstance(h,int)) #False

