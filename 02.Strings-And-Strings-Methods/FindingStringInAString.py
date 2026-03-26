####                Finding a String in a String                ####

"""
One of the most useful string methods is .find(). As its name implies,
you can use this method to find the location of one string in another
string—commonly referred to as a substring.

To use .find(), tack it to the end of a variable or a string literal and
pass the string you want to find in between the parentheses:

"""
phrase = "The surprise is in here somewhere"
#print(phrase.find("here"))
#print(phrase.find("surprise"))

"""
The value that .find() returns is the index of the first occurrence of the
string you pass to it. In this case, "surprise" starts at the fifth character
of the string "the surprise is in here somewhere" which has index 4
because counting starts at 0.

If .find() doesn’t find the desired substring, it will return -1 instead:
"""
#print(phrase.find("suprise"))
#print(phrase.find("what"))



"""
You can call string methods on a string literal directly, so in this case,
you don’t need to create a new string:
"""
#phrase = "The surprise is in here somewhere".find("here")
#print(phrase)



"""
Keep in mind that this matching is done exactly, character by character, 
and is case-sensitive. For example, if you try to find "SURPRISE",
the .find() method returns -1:
"""
#print(phrase.find("SURPRISE"))




"""
If a substring appears more than once in a string, .find() only returns
the index of the first appearance, starting from the beginning of the
string:
"""

phrase2 = "The future is in the future live the present now"
#print(phrase2.find("future"))




"""
The .find() method only accepts a string as its input. If you want to
find an integer in a string, you need to pass the integer to .find() as a
string. If you do pass something other than a string to .find(), Python
raises a TypeError:
"""

#number = "My number is: +0952421267".find(5)
#print(number)

number = "My number is: +0952421267"
#print(number.find(5))

#print(number.find("5"))





####                .replace() method on a strings
"""
Sometimes you need to find all occurrences of a particular substring
and replace them with a different string. Since .find() only returns the
index of the first occurrence of a substring, you can’t easily use it to
perform this operation. 
Fortunately, string objects have a .replace() method that replaces each instance 
of a substring with another string.
Just like .find(), you tack .replace() on to the end of a variable or
string literal. In this case, though, you need to put two strings inside
of the parentheses in .replace() and separate them with a comma. The
first string is the substring to find, and the second string is the string
to replace each occurrence of the substring with.

For example, the following code shows how to replace each occurrence of "the truth" in the string "I'm telling you the truth; nothing
but the truth" with the string "lies":

"""
truth = "I'm telling you the truth; nothing but the truth!"
#print(truth)

#print(truth.replace("truth", "future"))


"""
Since strings are immutable objects, .replace() doesn’t alter truth.
If you immediately print into the interactive window after runni-ng 
the above example, you’ll see the original string, unaltered:
"""
#print(truth)



"""
To change the value of truth, you need to reassign to it the new
value returned by .replace():
"""
truth = truth.replace("truth", "future")
#print(truth)




"""
.replace() can only replace one substring at a time, so if you want to
replace multiple substrings in a string you need to use .replace() multiple times.
"""
text = "some of the stuff"
repText = text.replace("some of", "All")
repText = repText.replace("the stuff", " Things")
#print(repText)




####                Tasks               ####
# 1. In one line of code, display the result of trying to .find() the substring "a" 
# in the string "AAA". The result should be -1.
A = "AAA"
#rint(A)
#print(A.find("a"))



# 2. Replace every occurrence of the character "s" with "x" in the string
# "Somebody said something to Samantha.".
phrase = "Somebody said something to Samantha"
#print(phrase)
#print(phrase.replace("s", "x"))
repPhrase = phrase.replace("s", "x")
repPhrase = repPhrase.replace("S", "X")
#print(repPhrase)


#3. Write and test a script that accepts user input using the input()
# function and displays the result of trying to .find() a particular
# letter in that input.
test = input("Enter Your Words User? : ")
test = test.find("u")
print(test)


####                End of Finding a String in a String                 ####