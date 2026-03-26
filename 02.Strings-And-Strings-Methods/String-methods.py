####                Manipulate Strings With Methods             ####

"""
Strings come bundled with special functions called string methods
that can be used to work with and manipulate strings. There are numerous string methods available, but we’ll focus on some of the most
commonly used ones.

In this section, you will learn how to:
• Convert a string to upper or lower case
• Remove whitespace from string
• Determine if a string begins and ends with certain characters

"""


#####                    Converting String Case                  #####

"""
Converting String Case
To convert a string to all lower case letters, you use the string’s .lower()
method. This is done by tacking .lower() on to the end of the string
itself:
>>> "Jean-luc Picard".lower()
'jean-luc picard'

The dot (.) tells Python that what follows is the name of a method—
the lower() method in this case.

"""
name = "SAINT CHAMAK"
#print(name)
#name = name.lower()
#print(name)
#print(name.lower()) # different way of printing it


"""
Note: We will refer to the names of string methods with a dot at the
beginning of them. So, for example, the .lower() method is written with a dot, 
instead of lower().
The reason we do this is to make it easy to spot functions that
are string methods, as opposed to built-in functions like print()
and type().
"""

"""
String methods don’t just work on string literals. You can also use the
.lower() method on a string assigned to a variable:
>>> name = "Jean-luc Picard"
>>> name.lower()
'jean-luc picard'
"""
#name = name.lower()
#print(name)



"""
The opposite of the .lower() method is the .upper() method, 
which converts every character in a string to upper case:
"""
#name = name.upper()
#print(name)

#print(name.upper()) # Different way of printing the value

"""
Compare the .upper() and .lower() string methods to the generalpurpose len() function 
Aside from the different results of these functions, 
the important distinction here is how they are used.

The len() function is a stand-alone function. If you want to determine
the length of a string, you call the len() function directly,
like this:
"""
#print(len(name))


"""
On the other hand, .upper() and .lower() must be used in conjunction
with a string. They do not exist independently.
"""
#####                   End of Converting String Case                   #####










#####                   Removing Whitespace From a String                   #####
"""
Removing Whitespace From a String
Whitespace is any character that is printed as blank space. 
This includes things like spaces and line feeds, which are special characters
that move output to a new line.

Sometimes you need to remove whitespace from the beginning or end
of a string. This is especially useful when working with strings that
come from user input, where extra whitespace characters may have
been introduced by accident.

There are three string methods that you can use to remove whitespace
from a string:
1. .rstrip()
2. .lstrip()
3. .strip()

"""


"""
.rstrip() removes whitespace from the right side of a string:
"""
# The best way to see the changes test this on python IDLE
name = "Saint Chamak     "
#print(name)
#print(name.rstrip()) # .rstring method implementation on a print function

#name = name.rstrip() # .rstring method implementation
#print(name)


"""
In this example, the string "Saint Chamak     " has five trailing spaces. 
Python doesn’t remove any trailing spaces in a string automatically 
when the string is assigned to a variable. 
The .rstrip() method removes trailing spaces from the right-hand side of the string
and returns a new string "Saint Chamak", which no longer has the spaces at the end.
"""



"""
The .lstrip() method works just like .rstrip(), except that it removes
whitespace from the left-hand side of the string:
"""
name = "     Saint Chamak"
#print(name)
#print(name.lstrip())

#name = name.lstrip()
#print(name)




"""
To remove whitespace from both the left and the right sides of the
string at the same time, use the .strip() method:
"""
name = "     Saint Chamak     "
#print(name)
#print(name.strip()) # .strip method implemented on a print function

#name = name.strip() # .strip method implemented on a variable itself.
#print(name)

"""
Note:
None of the .rstrip(), .lstrip(), and .strip() methods remove
whitespace from the middle of the string. 
In each of the previous examples the space between “Saint” and “Chamak” is
always preserved.
"""
#####                   End of removing Whitespaces from a string                   #####










#####                   Determine if a string Starts or Ends with a Particular String                   #####
"""
When you work with text, sometimes you need to determine if a given
string starts with or ends with certain characters. You can use two
string methods to solve this problem: .startswith() and .endswith().
Let’s look at an example. Consider the string "Enterprise". Here’s how
you use .startswith() to determine if the string starts with the letters
e and n:

"""
word = "Enterprise"
#print(word)
#print(word.startswith("en")) # .startswith() method implemented on a print function

#word = word.startswith("en") # .startswith() method implemented on a variable.
#print(word)

"""
You must tell .startswith() what characters to search for by providing
a string containing those characters. So, to determine if "Enterprise"
starts with the letters e and n, you call .startswith("en"). This returns
False. Why do you think that is?

"""


"""
If you guessed that .startswith("en") returns False because 
"Enterprise" starts with a capital E, you’re absolutely right! The .startswith()
method is case-sensitive. 
To get .startswith() to return True, you need to provide it with the string "En":

"""
#print(word)
#print(word.startswith("En"))

#word = word.startswith("En")
#print(word)



"""
The .endswith() method is used to determine if a string ends
with certain characters:
"""
#print(word)
#print(word.endswith("rise")) # .endswith implimentated on a print function

#word = word.endswith("rise") # .endswith implemented on a variable
#print(word)


"""
Just like .startswith(), the .endswith() method is case-sensitive:
"""
#print(word)
#print(word.endswith("risE"))

#word = word.endswith("risE")
#print(word)


"""
Note:
The True and False values are not strings. They are a special kind
of data type called a Boolean value. 
"""

#####                   End of Determine if a string Starts or Ends with a Particular String                    #####










#####                   String Methods and Immutability                 #####

"""
String Methods and Immutability
Recall from the previous section that strings are immutable—they
can’t be changed once they have been created. Most string methods
that alter a string, like .upper() and .lower(), actually return copies of
the original string with the appropriate modifications.
If you aren’t careful, this can introduce subtle bugs into your program.

Try this out in IDLE’s interactive window:
>>> name = "Picard"
>>> name.upper()
'PICARD'
>>> name
'Picard'

"""
name = "Saint Chamak"
#print(name)
#print(name.upper())

#print(name)

"""
When you call name.upper(), nothing about name actually changes. If
you need to keep the result, you need to assign it to a variable:
"""
#print(name)
#name = name.upper()
#print(name)

"""
name.upper() returns a new string "SAINT CHAMAK", which is re-assigned to the
name variable. This overrides the original string "Saint Chamak" assigned to
"name"
"""

#####                   End of String Methods and Immutability                  #####











#####                   Using IDLE to Discover Additional String Methods                    #####

"""
Strings have lots of methods associated to them. 
The methods introduced in this section barely scratch the surface. 
IDLE can help you find new string methods. To see how, 
first assign a string literal to a variable in the interactive window:

"""
name = "Saint Chamak"

"""
Next, type NameOfTheVariable followed by a period, but do not hit Enter. You
should see the following in the interactive window:

name.
"""
# This works easly on a IDE such as VSCode but on actual IDLE using Tab after period
# can be the go to method if you want to see different options of methods available.

#name = name.
#print(name)

"""
Now wait for a couple of seconds. IDLE displays a list of every string
method that you can scroll through with the arrow keys.
A related shortcut in IDLE is the ability to fill in text automatically
without having to type in long names by hitting Tab. 
For instance, if you only type in starship.u and then hit the Tab key, 
IDLE automatically fills in starship.
upper because there is only one method belonging
to starship that begins with a u.

This even works with variable names. Try typing in just the first few
letters of VariableName and, assuming you don’t have any other names already defined 
that share those first letters, IDLE completes the VariableName for you 
when you hit the Tab key.
"""

####                Tasks
# Write a script that converts the following strings to lowercase: "Animals", 
# "Badger", "Honey Bee", "Honeybadger". Print each lowercase string on a 
# separate line.

words = ["Animals", "Badger", "Honey Bee", "Honeybadger"] # Array of the strings in one variable
# Printing them in lowercase
print(words[0].lower())
print(words[1].lower())
print(words[2].lower())
print(words[3].lower())

# Printing them in Uppercase
print(words[0].upper())
print(words[1].upper())
print(words[2].upper())
print(words[3].upper())




# Write a script that removes whitespace from the following strings:
string1 = "     Filet Mignon"
print(string1)
print(string1.lstrip())


string2 = "Brisket      "
print(string2)
print(string2.rstrip())


string3 = "     Cheeseburger    "
print(string3)
print(string3.strip())




# Write a script that prints out the result of .startswith("be") on each 
# of the following strings:
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful" # Remember the space to

# Returns True and False depending on the argument
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))



# return True for all argument
print(string1.startswith("Be"))
print(string2.startswith("be"))
print(string3.startswith("BE"))
print(string4.startswith(" bE")) # Space sensitive

#####                   End of String Methods                   #####
