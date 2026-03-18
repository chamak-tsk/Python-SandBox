"""
Docstring for 02.Strings-And-Strings-Methods.Concatenation-Indexing-Slicing

In this section, you’ll learn about three basic string operations:
1. Concatenation, which joins two strings together
2. Indexing, which gets a single character from a string
3. Slicing, which gets several characters from a string at once

"""



####                Strings Concatenation               ####

"""
Two strings can be combined, or concatenated, using the + operator:

"""
PhareOne = "Abra"
PhareTwo = "cadabra"
MagicPhrase = PhareOne + PhareTwo

#print(MagicPhrase)
#print(f"{PhareOne} {PhareTwo}") # My prefered way of doing it

"""
In this example, string concatenation occurs on the third line. PhraseOne
and PhraseTwo are concatenated using + and the result is assigned to the
variable MagicPhrase. Notice that the two strings are joined without
any whitespace between them.

You can use string concatenation to join two related strings, such as
joining a first and last name into a full name:

"""

FirstName = "Franklin"
LastName = "Saint"

FullName = FirstName + " " + LastName

#print(FullName)
#print(f"{FirstName} {LastName}") # My prefered way of doing it





####             String Indexing             ####
"""
Each character in a string has a numbered position called an index.
You can access the character at the Nth position by putting the number N 
in between two square brackets ([ and ]) immediately after the
string:

"""

Flavour = "Apple Pie"
#print(Flavour[0])
#print(Flavour[1])
#print(Flavour[2])
#print(Flavour[3])
#print(Flavour[4])
#print(Flavour[5])
#print(Flavour[6])
#print(Flavour[7])
#print(Flavour[8])

"""
flavor[1] returns the character at position 1 in "Apple Pie", which is p.
Wait, isn’t a the first character of "Apple Pie"?
In Python—and most other programming languages—counting
always starts at zero. To get the character at the beginning of a string,
you need to access the character at position 0:

"""

"""
Note
Forgetting that counting starts with zero and trying to access
the first character in a string with the index 1 results in an oпby-one error.
Off-by-one errors are a common source of frustration for both
beginning and experienced programmers alike!

The following figure shows the index for each character of the string
"Apple Pie":
| A | p | p | l | e | | P | i | e |
  0   1   2   3   4  5  6   7   8
"""

"""
If you try to access an index beyond the end of a string, Python raises
an IndexError:

"""
#print(Flavour[9])

"""
The largest index in a string is always one less than the string’s length.
Since "Apple Pie" has a length of nine, the largest index allowed is 8.
"""

"""
Strings also support negative indices:
"""
#print(Flavour[-1])
#print(Flavour[-2])
#print(Flavour[-3])
#print(Flavour[-4])
#print(Flavour[-5])
#print(Flavour[-6])
#print(Flavour[-7])
#print(Flavour[-8])
#print(Flavour[-9])


"""
The last character in a string has index -1, which for "Apple Pie" is the
letter e. The second-to-last character i has index -2, and so on.

The following figure shows the negative index for each character in
the string "Apple Pie":

| a | p | p | l | e | | p | i | e |
 -9  -8  -7  -6  -5 -4 -3  -2  -1

"""

"""
Just like positive indices, Python raises an IndexError if you try to access a negative index less than the index of the first character in the
string:
"""
#print(Flavour[-10])


"""
Negative indices may not seem useful at first, but sometimes they are
a better choice than a positive index.

For example, suppose a string input by a user is assigned to the variable 
user_input. If you need to get the last character of the string, how
do you know what index to use?
One way to get the last character of a string is to calculate the final
index using len():
"""
#UserInput = input("Enter Your Names:")
#FinalIndex = len(UserInput) - 1
#LastCharactersFormat1 = UserInput[FinalIndex]
#LastCharactersFormat2 = UserInput[-1]
#print(FinalIndex)
#print(LastCharactersFormat1)
#print(LastCharactersFormat2)






####                String Slicing              ####
"""
Suppose you need the string containing just the first three letters of
the string "Apple Pie". You could access each character by index and
concatenate them, like this:
"""
FirstThreeLetters = Flavour[0] + Flavour[1] + Flavour[2]
#print(FirstThreeLetters)

"""
Getting the final character with the index -1 takes less typing and
doesn’t require an intermediate step to calculate the final index:
"""

"""
If you need more than just the first few letters of a string, getting each
character individually and concatenating them together is clumsy
and long-winded. Fortunately, Python provides a way to do this with
much less typing.

You can extract a portion of a string, called a substring, by inserting a
colon between two index numbers inside of square brackets, like this:
"""
SubString = Flavour[0:3]
#print(SubString)



"""
Flavor[0:3] returns the first three characters of the string assigned to
Flavor, starting with the character with index 0 and going up to, but not
including, the character with index 3. The [0:3] part of Flavor[0:3] is
called a slice. In this case, it returns a slice of "Apple Pie". Yum!

String slices can be confusing because the substring returned by
the slice includes the character whose index is the first number, but
doesn’t include the character whose index is the second number.

To remember how slicing works, you can think of a string as a 
sequence of square slots. The left and right boundary of each slot is
numbered from zero up to the length of the string, and each slot is
filled with a character in the string.
Here’s what this looks like for the string "apple pie":
| a | p | p | l | e | | p | i | e |
  0   1   2   3   4  5  6   7   8   9

The slice [x:y] returns the substring between the boundaries x and y.
So, for "Apple Pie", the slice [0:3] returns the string "App", and the slice
[3:9] returns the string "le Pie".
"""
#print(Flavour[3:9])

"""
If you omit the first index in a slice, Python assumes you want to start
at index 0:
"""

#print(Flavour[:3])
#print(Flavour[:5])
#print(Flavour[:9])

"""
The slice [:5] is equivalent to the slice [0:5], so flavor[:5] returns the
first five characters in the string "Apple Pie".

Similarly, if you omit the second index in the slice, Python assumes
you want to return the substring that begins with the character whose
index is the first number in the slice and ends with the last character
in the string:

"""
#print(Flavour[5:])

"""
For "Apple Pie", the slice [5:] is equivalent to the slice [5:9]. Since
the character with index 5 is a space, Flavor[5:9] returns the substring
that starts with the space and ends with the last letter, which is " Pie".

"""

"""
If you omit both the first and second numbers in a slice, you get a
string that starts with the character with index 0 and ends with the last
character. In other words, omitting both numbers in a slice returns
the entire string:

"""
#print(Flavour[:])

"""
It’s important to note that, unlike string indexing, Python won’t raise
an IndexError when you try to slice between boundaries before or after 
the beginning and ending boundaries of a string:
"""

#print(Flavour[:14])
#print(Flavour[13:15])

"""
In this example, the first line gets the slice from the beginning of the
string up to but not including the fourteenth character. The string assigned to flavor has length nine, so you might expect Python to throw
an error. Instead, any non-existent indices are ignored and the entire
string "Apple Pie" is returned.

The second shows what happens when you try to get a slice where
the entire range is out of bounds. Flavor[13:15] attempts to get the
thirteenth and fourteenth characters, which don’t exist. Instead of
raising an error, the empty string "" is returned.
"""




"""
You can use negative numbers in slices. 
The rules for slices with negative numbers are exactly the same as 
slices with positive numbers.

It helps to visualize the string as slots with the boundaries labeled by
negative numbers:
| a | p | p | l | e | | p | i | e |
 -9  -8  -7  -6  -5 -4 -3  -2  -1

Just like before, the slice [x:y] returns the substring between the
boundaries x and y. For instance, the slice [-9:-6] returns the first
three letters of the string "apple pie":
"""
#print(Flavour[-9:-6])



"""
Notice, however, that the right-most boundary does not have a negative index. 
The logical choice for that boundary would seem to be the
number 0, but that doesn’t work:
"""
#print(Flavour[-9:0])

"""
Instead of returning the entire string, [-9:0] returns the empty
string "". This is because the second number in a slice must correspond to a boundary that comes after the boundary corresponding
to the first number, but both -9 and 0 correspond to the left-most
boundary in the figure.
"""


"""
If you need to include the final character of a string in your slice, you
can omit the second number:
"""
#print(Flavour[-9:])




"""
Strings Are Immutable
To wrap this section up, let’s discuss an important property of string
objects. Strings are immutable, which means that you can’t change
them once you’ve created them. For instance, see what happens when
you try to assign a new letter to one particular character of a string:
"""
Word = "Goal"
#Word[0] = "T"
#print(Word)

"""
Python throws a TypeError and tells you that str objects don’t support
item assignment.
"""

"""
Note:
The term str is Python’s internal name for the string data type.
If you want to alter a string, you must create an entirely new string.

To change the string "Goal" to the string "Toal", you can use a string
slice to concatenate the letter "T" with everything but the first letter of
the word "Goal":
"""

Word = "Goal"
Word = "T" + Word[1:]
#print(Word)

"""
First assign the string "Goal" to the variable word. Then concatenate
the slice word[1:], which is the string "oal", with the letter "T" to get
the string "Toal". If you’re getting a different result here, make sure
you’re including the : colon character as part of the string slice.

"""




####        Tasks       ####
##### Create a string and print its length using the len() function.
Agent = "The distribution of agents makes it easier to separate tasks."
#print(len(Agent))



##### Create two strings, concatenate them, and print the resulting string.
FirstName = "Franklin"
LastName = "Saint"
FullName = FirstName + LastName

print(FullName)
print(f"{FirstName} {LastName}")
print(FirstName + " " + LastName)




##### Print the string "zing" by using slice notation on the string
# "bazinga" to specify the correct range of characters.
Word = "Bazinga"

print(Word)
print(Word[2:6])



#####           -----         -----         -----         #####