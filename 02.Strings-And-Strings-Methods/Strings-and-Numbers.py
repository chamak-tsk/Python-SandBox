####                   Working with Strings and Numbers             ####

"""
When you get user input using the input() function, the result is always
a string. There are many other times when input is given to a program
as a string. Sometimes those strings contain numbers that need to be
fed into calculations.

In this section you will learn how to deal with strings of numbers. You
will see how arithmetic operations work on strings, and how they often
lead to surprising results. You will also learn how to convert between
strings and number types.

"""

"""
Strings and Arithmetic Operators
You’ve seen that string objects can hold many types of characters, 
including numbers. However, don’t confuse numerals in a string with
actual numbers. For instance, try this bit of code out in IDLE’s interactive window:

"""
#numb = "2"
#numb = numb + numb
#print(numb)


"""
The + operator concatenates two string together. So, the result of "2"
+ "2" is "22", not "4".

Strings can be “multiplied” by a number as long as that number is
an integer, or whole number. Type the following into the interactive
window:

"""
#numb = "12"
#numb = numb * 3
#print(numb)




"""
num * 3 concatenates the string "12" with itself three times and returns
the string "121212". To compare this operation to arithmetic with numbers, notice that "12" * 3 = "12" + "12" + "12". In other words, multiplying a string by an integer n concatenates that string with itself n
times.
The number on the right-hand side of the expression num * 3 can be
moved to the left, and the result is unchanged:

"""
#numb = "12"
#numb = 3 * numb
#print(numb)




"""
If you use the * operator between two
strings such as "12" * "3" a TypeError will occur 
"""
#numb = "12"
#numb2 = "3"
#Totalnumb = numb * numb2
#print(Totalnumb)

"""
Python raises a TypeError and tells you that you can’t multiply a sequence by a 
non-integer. Because when the * operator is used with a string
on either the left or the right side, it always expects an integer on the
other side.
"""



"""
Note:
A sequence is any Python object that supports accessing elements by index. 
Strings are sequences.
"""



##### Adding string and number
numb = "3"
numb2 = 3
#Total = numb + numb2
#print(Total)

"""
Trying to add a string and number will also throw a TypeError
because the + operator expects both
things on either side of it to be of the same type. If any one of the
objects on either side of + is a string, Python tries to perform string
concatenation. Addition will only be performed if both objects are
numbers. So, to add "3" + 3 and get 6, you must first convert the
string "3" to a number.

"""
#numb1 = int(numb)
#Totalnumb = numb1 + numb2
#print(Totalnumb)




#####                   Converting Strings to Numbers                   #####
"""
Converting Strings to Numbers
The TypeError errors you saw in the previous section highlight a common problem 
encountered when working with user input: type mismatches when trying to use the 
input in an operation that requires a number and not a string.
"""

#numb = input("Enter a number to be doubled: ")
#doubledNumb = numb * 2
#print(f"The number is: {doubledNumb}")

"""
When you enter a number, such as 2, you expect the output to be 4, but
in this case, you get 22. Remember, input() always returns a string, so
if you input 2, then num is assigned the string "2", not the integer 2.
Therefore, the expression num * 2 returns the string "2" concatenated
with itself, which is "22".
"""

"""
To perform arithmetic on numbers that are contained in a string, you
must first convert them from a string type to a number type. There
are two ways to do this: int() and float().
int() stands for integer and converts objects into whole numbers,
while float() stands for сoating-point number and converts objects into numbers with decimal points. Here’s what using them looks
like.
"""

#numb = "12"
#numb = int(numb)
#print(numb, type(numb))

#numb = float(numb)
#print(numb, type(numb))

"""
Notice how float() adds a decimal point to the number. 
Floatingpoint numbers always have at least one decimal place of precision. 
For this reason, you can’t change a string that looks like a floating-point
number into an integer because you would lose everything after the
decimal point:
"""
#numb = "12.0"
#numb = int(numb)
#print(numb, type(numb)) # ValueError 

"""
Even though the extra 0 after the decimal place doesn’t add any value to the number, 
Python won’t change 12.0 into 12 because it would result in the loss of precision.
"""

"""
Let’s revisit the script from the beginning of this section and see how
to fix it. Here’s the script again:

The issue lies in the line doubledNumb = numb * 2 because numb references
a string and 2 is an integer. 
You can fix the problem by wrapping numb with either int() or float(). 
Since the prompts asks the user to input a number, and not specifically an integer, 
let’s convert num to a floatingpoint number:

Now when you run this script and input 2, you get 4.0 as expected.
"""
#numb = input("Enter a number to be doubled: ")
#doubledNumb = float(numb) * 2
#print(f"The number is: {doubledNumb}")

#####                   End of Converting Strings to Numbers                    #####






#####                   Converting Numbers to Strings                   #####
"""
Converting Numbers to Strings
Sometimes you need to convert a number to a string. You might do this, 
for example, if you need to build a string from some pre-existing
variables that are assigned to numeric values.
As you’ve already seen, the following produces a TypeError:
"""
#numbOfPancakes = 10
#print("I am going to eat " + numbOfPancakes + "Pancakes") # TypeError

"""
Since numOfPancakes is a number, Python can’t concatenate it with the
string "I'm going to eat". To build the string, you need to convert
numOfPancakes to a string using str():
"""

#numbOfPancakes = str(numbOfPancakes)
#print("I am going to eat" + " " + numbOfPancakes + " " + "Pancakes")

"""
str() can even handle arithmetic expressions:
"""
#totalNumbOfPancakes = 10
#pancakesEaten = 5
#print(f" Remained Pancakes are: {str(totalNumbOfPancakes - pancakesEaten)} pancakes")

"""
You’re not limited to numbers when using str(). You can pass it all sorts of objects
to get their string representations:

>>> str(print)
'<built-in function print>'
>>> str(int)
"<class 'int'>"
>>> str(float)
"<class 'float'>"

These examples may not seem very useful, but they illustrate how flexible str() is.

"""





#### Tasks

# 1. Create a string containing an integer, then convert that string into
# an actual integer object using int(). Test that your new object is
# a number by multiplying it by another number and displaying the
#result.

#numb = "2"
#print(numb, type(numb))

#numb = int(numb)
#print(numb, type(numb))

#numbMultplied = numb * 2
#print(f"{numbMultplied} {type(numbMultplied)}")



#2. Repeat the previous exercise, but use a floating-point number and
#float().

#numb = "2.0"
#print(f"{numb}, {type(numb)}")

#numb = float(numb)
#print(f"{numb} {type(numb)}")

#numbFloat = numb * 2.0
#print(f"{numbFloat} {type(numbFloat)}")




#3. Create a string object and an integer object, then display them sideby-side 
# with a single print statement by using the str() function.
#numb = "2"
#numb2 = 2
#print("String object and Integer object side by side: " + " " + str(numb) + " " + str(numb2))
#print(f"String object and Integer object side by side: {numb} {type(numb)} {numb2} {type(numb2)}")



#4. Write a script that gets two numbers from the user using the
#input() function twice, multiplies the numbers together, and
#displays the result. If the user enters 2 and 4, your program should
#print the following text:

numb = input("Enter the First Number: ")
numb2 = input("Enter the Second Number: ")

numb = int(numb)
numb2 = int(numb2)

product = numb * numb2
print(f"The product of the two numbers is: {product} {type(product)}" )

#####                   End of Strings and Numbers                  #####