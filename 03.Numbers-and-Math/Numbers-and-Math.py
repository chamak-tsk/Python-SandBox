###             Numbers and Math

"""
You don’t need to be a math whiz to program well. The truth is, 
few programmers need to know more than basic algebra.
Of course, how much math you need to know depends on the application you are 
working on. In general, the level of math required to successfully work as 
a programmer is less than you might expect.

Although math and computer programming aren’t as correlated as some people might
believe, numbers are an integral part of any programming language and 
Python is no exception.

In this chapter, you will learn how to:
• Work with Python’s three built-in number types: integer, floatingpoint, and 
complex numbers.
• Round numbers to a given number of decimal places.
• Format and display numbers in strings.

Let’s get started!

"""





##### Intergers and Floating-Point Numbers                  #####

"""
Python has three built-in number data types: integers, floating-point
numbers, and complex numbers. 
In this section, you’ll learn about integers and floating-point numbers, 
which are the two most commonly used number types.
"""



#####                   Intergers Numbers                   #####
"""
Integers
An integer is a whole number with no decimal places. For example,
1 is an integer, but 1.0 isn’t. The name for the integer data type is int,
which you can see with the type() function:
"""
numb = 1 #Int
numbTwo = 1.0 #Float
#print(f"{numb} is a {type(numb)} data type")
#print(f"{numbTwo} is a {type(numbTwo)} data type")

"""
You can create an integer by simply typing the number explicitly or
using the int() function.
"""
numb = "1"
numb = int(numb)
#print(f"{numb} is a {type(numb)} data type")


"""
An integer literal is an integer value that is written explicitly in your
code, just like a string literal is a string that is written explicitly in your
code. For example, 1 is an integer literal, but int("1") isn’t.
"""

"""
Integer literals can be written in two different ways:
>>> 1000000
1000000
>>> 1_000_000
1000000

"""



"""
The first example is straightforward. Just type a 1 followed by six zeros. 
The downside to this notation is that large numbers can be difficult to read.
When you write large numbers by hand, you probably group digits
into groups of three, separated by a comma. 1,000,000 is a lot easier
to read than 1000000.

In Python, you can’t use commas to group digits in integer literals,
but you can use an underscore (_). The value 1_000_000 expresses one
million in a more readable manner.
There is no limit to how large an integer can be, which might be
surprising considering computers have finite memory. Try typing
the largest number you can think of into IDLE’s interactive window.
Python can handle it with no problem!
"""

#####                   End of Intergers Numbers                    #####






#####                   Floating-Point Numbers                  #####

"""
A floating-point number, or float for short, is a number with a
decimal place. 1.0 is a floating-point number, as is -2.75. The name
of a floating-point data type is float:
"""
number = 1.0
#print(f"{number} is a {type(number)} -point number")

"""
Floats can be created by typing a number directly into your code, or by
using the float() function. Like int(), float() can be used to convert
a string containing a number to a floating-point number
"""
number = 2
numberTwo = 1.2

#print(f"{number} is a {type(number)} type")
#print(f"{numberTwo} is a {type(numberTwo)} type")

numberTwo = float(numberTwo)
#print(f"{numberTwo} is a {type(numberTwo)} type")


"""
A floating-point literal is a floating-point value that is written explicitly
in your code. 
1.25 is a floating-point literal, while float("1.25") is not.
Floating-point literals can be created in three different ways.
"""

numberOne = 1000000.0
numberTwo = 1_000_000.0
numberThree = 1e6

#print(f"{numberOne} is a {type(numberOne)} type")
#print(f"{numberTwo} is a {type(numberTwo)} type")
#print(f"{numberThree} is a {type(numberThree)} type")

"""
The first two ways are similar to the two methods for creating integer
literals that you saw earlier. The second method, which uses underscores 
to separate digits into groups of three, is useful for creating float literals 
with lots of digits.

For really large numbers, you can use E-notation. The third method
in the previous example uses E-notation to create a float literal.
To write a float literal in E-notation, type a number followed by the
letter e and then another number. Python takes the number to the
left of the e and multiplies by 10 raised to the power of the number
after the e. So 1e6 is equivalent to 1×10⁶.
"""

"""
Note:
E-notation is short for exponential notation, and is the more
common name for how many calculators and programming languages 
display large numbers.
"""

numberFour = 7000000000000000000000000000.0
#print(f"{numberFour} is a {type(numberFour)} type")

"""
The + sign indicates that the exponent 27 is a positive number. You can also use
negative numbers as the exponent
"""
numberFive = 1e-4
#print(f"{numberFive} is a {type(numberFive)} type")

numberFive = 0.00000000000000000000000000001
#print(f"{numberFive} is a {type(numberFive)} type")


"""
The literal 1e-4 is interpreted as 10 raised to the power -4, which is
1/10000 or, equivalently, 0.0001.

Unlike integers, floats do have a maximum size. The maximum
floating-point number depends on your system, but something like
2e400 ought to be well beyond most machines’ capabilities. 2e400 is
2×10⁴⁰⁰, which is far more than the total number of atoms in the
universe!

When you reach the maximum floating-point number, Python returns
a special float value inf:

inf stands for infinity, and it just means that the number you’ve tried
to create is beyond the maximum floating-point value allowed on your
computer. The type of inf is still float.
"""
numberSix = 2e400
numberSeven = 7e2000
#print(f"{numberSix} is a {type(numberSix)} type")
#print(f"{numberSeven} is a {type(numberSeven)} type")

"""
There is also -inf which stands for negative infinity, and represents a
negative floating-point number that is beyond the minimum floatingpoint 
number allowed on your computer:
"""
numberEight = -2e400
#print(f"{numberEight} is a {type(numberEight)} type")




####                Tasks               ####

#1. Write a script that creates the two variables, num1 and num2. Both
#num1 and num2 should be assigned the integer literal 25,000,000,
#one written with underscored and one without. Print num1 and num2
#on two separate lines.

numb1 = 25000000
numb2 = 25_000_000
print(f"{numb1} is a {type(numb1)} type")
print(f"{numb2} is a {type(numb2)} type")




#2. Write a script that assigns the floating-point literal 175000.0 to the
#variable num using exponential notation, and then prints num in the
#interactive window.

floatPointLiteral = 175e3
print(f"{floatPointLiteral} is a {type(floatPointLiteral)} type")




#3. In IDLE’s interactive window, try and find the smallest exponent N
#so that 2e<N>, where <N> is replaced with your number, returns inf.
infNumber = 2e308 #Inf may start from 307 --->
print(f"{infNumber} is a {type(infNumber)} type")






####                    End of Floating-Point Numbers               ####
