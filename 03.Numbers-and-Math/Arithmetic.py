#Python as a calculator
#Basic Operator
"""
is a symbol of the programming language, which is able to operate on the values.
                (+) Addition
                (-) Substraction
                (*) Multiplication
                (/) Division
                (//) Interger Division (floor division)
                (%) Reminder(Modulo)
                (**) Exponentiation

                Remember: Data and operators when connected together form expressions. The simplest expression is a literal itself.
"""

            ###(+) Addition
#print(1 + 4)

#print(-4 + 4)
#print(-4. + 8)
#print(+2)

#a = 1
#b = 3
#print(a+b)

            ###(-) Substraction
#print(5 - 10)
#print(3.5 - 6.4)

#print(-4 - 4)
#print(4. - 8)
#print(-1.1)

#c = 10
#d = 5
#print(c - d)


            ###(**) Exponentiation
#print(5 ** 2)
#print(2 ** 3.)
#print(2. ** 3)
#print(2. ** 3.)

"""
    - For Readability put a space between the operator and the value, but it's not compulsory.

    Remember: It's possible to formulate the following rules based on this result:
        - when both ** arguments are integers, the result is an integer, too;
        - when at least one ** argument is a float, the result is a float, too.
    This is an important distinction to remember.

"""

            ###(*) Multiplication
#print(9 * 10)
#print(9 * 10.)
#print(9. * 10)
#print(9. * 10.)


            ###(/) Division
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

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

"""
        Subexpressions in parentheses are always calculated first.
                                                 E.x 15 - 1 * (5 * (1 + 2)) = 0.
"""
print((2 ** 4), (2 * 4.), (2 * 4))

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

print((2 % -4), (2 % 4), (2 ** 3 ** 2))