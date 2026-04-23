###             Arithmetic Operations and Expression            ###

"""
This section explains about the Fundamental of arithmetic operations in Python, 
such as addition, subtraction, multiplication, and division. 
And their expressions.

Along the way, you’ll learn some conventions for writing mathematical expressions
in code.
"""

####                Basic Operator              ####
"""
is a symbol of the programming language, which is able to operate on the values.
    (+) Addition
        (-) Substraction
            (*) Multiplication
                    (/) Division
                        (//) Interger Division (floor division)
                            (%) Reminder(Modulo)
                                (**) Exponentiation

Remember: Data and operators when connected together form expressions. 
The simplest expression is a literal itself.
"""





####                 (+) Addition                   ####

"""
Addition is performed with the + operator:
"""
numberOne = 1
numberTwo = 4
totalOfTwoNumbers = numberOne + numberTwo
#print(totalOfTwoNumbers)

"""
The two numbers on either side of the + operator are called operands.
In the previous example, both operands are integers, but operands do
not need to be the same type. You can add an int to a float with no
problem:
"""
numberThree = 2.7
totalOfTwoNumbers_OneIsAFloat = numberOne + numberThree
#print(f"{totalOfTwoNumbers_OneIsAFloat} which is a {type(totalOfTwoNumbers_OneIsAFloat)}")

"""
Notice that the result is a float. 
Any time a float is added to a number, the result is another float. 

Adding two integers together always results in an int.
"""
#####   Addition operation between a positive and negative intergers and float-point numbers
negativeNumber = -4
positiveNumber = 4
totalOfTwoNumbers = negativeNumber + positiveNumber
#print(f"{totalOfTwoNumbers} which is a {type(totalOfTwoNumbers)}")



floatingPoint_NegativeNumber = -4.
intergerNumber = 8
totalOfTwoNumbers = floatingPoint_NegativeNumber + intergerNumber
#print(f"{totalOfTwoNumbers} which is a {type(totalOfTwoNumbers)}")



positiveNumber = +2
#print(f"{positiveNumber}")


"""
Note:
PEP 8 recommends separating both operands from an operator
with a space.

Python can evaluate 1+1 just fine, but 1 + 1 is the preferred format because
it’s generally considered easier to read. 
This rule of thumb applies to all of the operators. 

So, for Readability put a space between the operator and the value, 
but it's not compulsory.

Remember: It's possible to formulate the following rules based on this result:
    - when both ** arguments are integers, the result is an integer, too;
    - when at least one ** argument is a float, the result is a float, too.
This is an important distinction to remember.

"""
####                 The End Of Addition                 ####






####                    (-) Substraction                ####

"""
To subtract two numbers, - operator is used.
"""
firstNumber = -10
secondNumber = 5
substractionOfTwoNumbers = firstNumber - secondNumber                  
#print(f"{substractionOfTwoNumbers} which is {type(substractionOfTwoNumbers)}")

"""
Just like adding two integers, subtracting two integers always results
in an int. 
Whenever one of the operands is a float, the result is also a float.
The - operator is also used to denote negative numbers:
>>>-7
"""
floatPoint_NegativeNumber = -6.4
floatingPoint_PositiveNumber = 3.5
substractionOfTwoNumbers = floatPoint_NegativeNumber - floatingPoint_PositiveNumber
#print(f"{substractionOfTwoNumbers} which is {type(substractionOfTwoNumbers)}")



#####   Denote negative number
#print(f"{-7} which is {type(-7)}")

number = -1.1
#print(f"{number} which is {type(number)}")



"""
You can subtract a negative number from another number, but as you
can see below, this can sometimes look confusing.
"""
firstNumber = -4
secondNumber = 4
substractionOfTwoNumbers = firstNumber - secondNumber
#print(f"{substractionOfTwoNumbers}")

substractionOfTwoNumbers = -4 - 4
#print(f"{substractionOfTwoNumbers} which is {type(substractionOfTwoNumbers)}")

substractionOfTwoNumbers = 1 - -3
#print(f"{substractionOfTwoNumbers} which is {type(substractionOfTwoNumbers)}")

substractionOfTwoNumbers = 1 --3
#print(f"{substractionOfTwoNumbers} which is {type(substractionOfTwoNumbers)}")

substractionOfTwoNumbers = 1--3
#print(f"{substractionOfTwoNumbers} which is {type(substractionOfTwoNumbers)}")


"""
Of the four examples above, the first and second are the most PEP 8 compliant.
That said, you can surround -3 with parentheses to make it even
clearer that the second - is modifying 3.
"""
substractionOfTwoNumbers = 1 - (-3)
#print(f"{substractionOfTwoNumbers} which is {type(substractionOfTwoNumbers)}")


"""
Using parentheses is a good idea because it makes the code more explicit. 
Computers execute code, but humans read code. 
Anything you can do to make your code easier to read and understand is a good
thing.
"""

####                    End of Substraction                 ####







####                    (*) Multiplication                  ####

"""
To multiply two numbers, use the * operator.
"""
multiplicationOfTwoNumbers = 9 * 10
#print(f"{multiplicationOfTwoNumbers} which is {type(multiplicationOfTwoNumbers)}")


"""
The type of number you get from multiplication follows the same rules
as addition and subtraction. Multiplying two integers results in an int,
and multiplying a number with a float results in a float.
"""
multiplicationOfTwoNumbers = 9 * 10.
#print(f"{multiplicationOfTwoNumbers} which is {type(multiplicationOfTwoNumbers)}")

multiplicationOfTwoNumbers = 9. * 10
#print(f"{multiplicationOfTwoNumbers} which is {type(multiplicationOfTwoNumbers)}")

multiplicationOfTwoNumbers = 9. * 10.
#print(f"{multiplicationOfTwoNumbers} which is {type(multiplicationOfTwoNumbers)}")

####                End of Multiplication                   ####






####                    (/) Division                ####
#print(4 / 2)
#print(4. / 2)
#print(4 / 2.)
#print(4. / 2.)
"""
    4 = Dividend
    2 = Divisor
    The answer is a quotient
    The remain of the division is a remainder

    The result produced by the division operator is always a float,
      regardless of whether or not the result seems to be a float at first glance: such as 1 / 2, 
      or if it looks like a pure integer: such as 2 / 1

    How not to divide:
        As you probably know, division by zero doesn't work.

        Do not try to:
            -perform a division by zero;
            -perform an integer division by zero;
            -find a remainder of a division by zero.

"""

            ###(//) Interger Division (floor division)
#print(4 // 2)
#print(4. // 2)
#print(4 // 2.)
#print(4. // 2.)
"""
        A (//) (double slash) sign is an integer division operator. It differs from the standard (/) operator in two details:

                    (i)    its result lacks the fractional part 
                                - it's absent (for integers).
                                - and it's always equal to zero (for floats). 
                        ***This means that the results are always rounded.
                    (ii)    it conforms to the integer vs. float rule.

            - integer by integer division gives an integer result. All other cases produce floats.

        *** This is very important: rounding always goes to the lesser integer.
                            The result of integer division is always rounded to the nearest integer value that is less than the real (not rounded) result.
"""
#print(4 // 3)

#print(-6 // 4) #output = -2
#print(6. // -4) #output = -2.0
"""
        Note: 
            some of the values are negative. This will obviously affect the result. But how?

                The result is two negative twos. The real (not rounded) result is -1.5 in both cases. 
                However, the results are the subjects of rounding.
                  The rounding goes toward the lesser integer value, 
                                and the lesser integer value is -2, hence: -2 and -2.0.

         Note:  
            Integer division can also be called floor division.
"""







            ###(**) Exponentiation
#print(5 ** 2)
#print(2 ** 3.)
#print(2. ** 3)
#print(2. ** 3.)






            ###(%) Remainder(Modulo)

"""
        The result of the operator is a remainder left after the integer division(//).
                In other words, it's the value left over after dividing one value by another to produce an integer quotient.
"""
#print(14 % 4)

#This little program kind helps to explain Remainder(Module) a little bit for integers

#Dividend = int(input("EnterfirstNumber:"))
#Advisor = int(input("EntersecondNumber:"))

#Quotient = Dividend // Advisor         #Quotent is the interger division/ floor division

#Q_remainder = Quotient * Advisor           #Q_remider is the result of multiplying the result of integer division/ floor division and the divisor

#Remainder = Dividend - Q_remainder

#print(Remainder)






#This little program kind helps to explain Remainder(Module) a little bit for floats
#Dividend = float(input("EnterfirstNumber:"))
#Advisor = float(input("EntersecondNumber:"))

#Quotient = Dividend // Advisor

#Q_remainder = Quotient * Advisor

#Remainder = Dividend - Q_remainder

#print(Remainder)



#Operators Binding

#MAGAZIJUTO (BODMAS)
#print(((1 + 3) * (9 - 2)/2)**2)

#print(9 % 6 % 2)

"""
There are two possible ways of evaluating this expression:

            from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1;
            from right to left: first 6 % 2 gives 0, and then 9 % 0 causes a fatal error.
            This operator has left-sided binding
"""

#print(2 ** 2 ** 3)

"""
            The two possible results are:

            2 ** 2 → 4; 4 ** 3 → 64
            2 ** 3 → 8; 2 ** 8 → 256

            Run the code. What do you see?

            The result clearly shows that the exponentiation operator uses right-sided binding.
"""


#print(-3 ** 2)
#print(-2 ** 3)
#print(-(3 ** 2))
 
"""
        A unary operator:
             is an operator with only one operand.
                                                E.x -1, or +3.

        A binary operator:
             is an operator with two operands.
                                                 E.x 4 + 5, or 12 % 5.

        Some operators act before others - the hierarchy of priorities:

                    - The (**) operator (exponentiation) has the highest priority.
                    - Then unary (+) and (-) (
                                                note: a unary operator to the right of the exponentiation operator binds more strongly.
                                                 for example 4 ** -1 equals 0.25)
                    - Then (*), (/) and (%),
                    - and finally, the lowest priority: binary + and -.
"""

#print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

"""
        Subexpressions in parentheses are always calculated first.
                                                 E.x 15 - 1 * (5 * (1 + 2)) = 0.
"""
#print((2 ** 4), (2 * 4.), (2 * 4))

#print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

#print((2 % -4), (2 % 4), (2 ** 3 ** 2))