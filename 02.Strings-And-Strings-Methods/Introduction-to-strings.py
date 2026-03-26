"""
Docstring for 02.Strings-And-Strings-Methods.StringsIntroduction

Collections of text in Python are called strings. 
Special functions called string methods are used to manipulate strings. 
There are string methods for changing a string from lowercase to uppercase, removing whitespace from the beginning or end of a string, or replacing
parts of a string with different text, and many more.

"""

"""
In this chapter, you will learn how to:
• Manipulate strings with string methods
• Work with user input
• Deal with strings of numbers
• Format strings for printing

"""


"""
The String Data Type
Strings are one of the fundamental Python data types. The term data
type refers to what kind of data a value represents. Strings are used
to represent text.

"""


"""
We say that strings are a fundamental data type because they can’t
be broken down into smaller values of a different type. Not all data
types are fundamental. You’ll learn about compound data types, also
known as data structures later.

The string data type has a special abbreviated name in Python: str.
You can see this by using the type() function, which is used to determine the data type of a given value.
"""
#type("Hello, World!")  # This will output: <class 'str'> when run on a Python interpreter

Phrase = "Hello, World!"
#print(type(Phrase))  # This will output: <class 'str'>


"""
Strings have three properties that are important to understand:
1. Strings contain characters, which are individual letters or symbols.
2. Strings have a length, which is the number of characters
contained in the string.
3. Characters in a string appear in a sequence, meaning each character has a numbered position in the string.
"""


"""
String Literals
As you’ve already seen, you can create a string by surrounding some
text with quotation marks:
string1 = 'Hello, world'
string2 = "1234"
Either single quotes (string1) or double quotes (string2) can be used
to create a string, as long as both quotation marks are the same type.
Whenever you create a string by surrounding text with quotation
marks, the string is called a string literal. The name indicates that
the string is literally written out in your code. 
"""



"""
NOTE: Not every string is a string literal. For example, a string captured as user input isn’t a string literal because it isn’t explicitly
written out in the program’s code.

"""


"""
The quotes surrounding a string are called delimiters because they
tell Python where a string begins and where it ends. When one type
of quotes is used as the delimiter, the other type of quote can be used
inside of the string:
"""
string3 = "We're #1!"
string4 = 'I said, "Put it over by the llama."'

"""
After Python reads the first delimiter, all of the characters after it are
considered a part of the string until a second matching delimiter is
read. This is why you can use a single quote in a string delimited by
double quotes and vice versa.
If you try to use double quotes inside of a string that is delimited by
double quotes, you will get an error:

Python throws a SyntaxError because it thinks that the string ends after
the second " and doesn’t know how to interpret the rest of the line.
"""
#text = "She said, "What time is it?""  # This will raise a SyntaxError when run on a Python interpreter



"""
Strings can contain any valid Unicode character. For example, the
string "We're #1!" contains the pound sign (#) and "1234" contains numbers. "×Pýŧħøŋ×" is also a valid Python string!
"""
string5 = "×Pýŧħøŋ×"
#print(string5)  # This will output: ×Pýŧħøŋ×







#### Length of a String
"""
Determine the Length of a String
The number of characters contained in a string, including spaces, is
called the length of the string. For example, the string "abc" has a
length of 3, and the string "Don't Panic" has a length of 11.
To determine a string’s length, you use Python’s built-in len() function,
which takes a string as its argument and returns the length of that string as an integer.
In the following example, len() is used to determine the lengths of two strings stored in variables:
Whether in a variable or directly as an argument, the len() function works the same way.
"""
Alphabet = "abc"
Pharase = "Don't Panic"

#print(len(Alphabet))       # This will output: 3
#print(len(Pharase))        # This will output: 11

# similarly, you can use the len() function to determine the length on a python interpreter
#print(len("abc"))          # This will output: 3
#print(len("Don't Panic"))  # This will output: 11

letters = "abcdefghijklmnopqrstuvwxyz"
LengthOfLetters = len(letters)
#print(LengthOfLetters)  # This will output: 26






#### Multiline Strings
"""
The PEP 8 style guide recommends that each line of Python code contain no more than 79 characters—including spaces.
When you have a long string that exceeds this limit, you can break it
into multiple lines by using multiline strings.

"""

"""
Note: PEP 8’s 79-character line-length is recommended because,
among other things, it makes it easier to read two files sideby-side. However, many Python programmers believe forcing
each line to be at most 79 characters sometimes makes code
harder to read.
"""

"""
One way is to break the string up across multiple lines and put a backslash (\) at the end of all but the last line. 
To be PEP 8 compliant, the total length of the line, including the backslash, must be 79 characters or less.
Here’s how you could write the paragraph as a multiline string using
the backslash method:

"""
paragraph = "This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."
#print(paragraph)


"""
Notice that you don’t have to close each line with a quotation mark.
Normally, Python would get to the end of the first line and complain
that you didn’t close the string with a matching double quote. With a
backslash at the end, however, you can keep writing the same string
on the next line.
When you print() a multiline string that is broken up by backslashes,
the output displayed on a single line:

"""

"""
Another way of implemeting Multiline strings is using triple quotes as delimiters

"""
paragraph2 = """This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy. """
print(paragraph2)

"""
Note: Triple-quoted strings have a special purpose in Python. They
are used to document code. You’ll often find them at the top
of a .py with a description of the code’s purpose. They are also
used to document custom functions.
When used to document code, triple-quoted strings are called
docstrings. 
"""

#####                   End of string introduction                  #####