####                Streamline Print Statements             ####

"""
Suppose you have a string human = "Human" and two integers heads = 1
and arms = 2. You want to display them in the following line: Human
has 1 head and 2 arms. This is called string interpolation, which is
just a fancy way of saying that you want to insert some variables into
specific locations in a string.
You’ve already seen two ways of doing this. The first involves using
commas to insert spaces between each part of the string inside of a
print() function:
"""
#human = "Human"
#head = 1
#arms = 2
#print(human, "has", str(head), "head and", str(arms), "Arms")

"""
Another way to do this is by concatenating the strings with the + operator:
"""
#print(human + " has " + str(head) + " Head and " + str(arms) + " Arms")



"""
Both techniques produce code that can be hard to read. Trying to keep
track of what goes inside or outside of the quotes can be tough. Fortunately, there’s a third way of combining strings: formatted string
literals, more commonly known as f-strings.

The easiest way to understand f-strings is to see them in action. Here’s
what the above string looks like when written as an f-string:

"""
#print(f"{human} has {head} head and {arms} Arms")

"""
There are two important things to notice about the above examples:
1. The string literal starts with the letter f before the opening quotation mark
2. Variable names surrounded by curly braces ({ and }) are replaced
with their corresponding values without using str()
You can also insert Python expressions in between the curly braces.
The expressions are replaced with their result in the string:
"""
#n = 3
#m = 4
#print(f"{n} times {m} is {n*m}")

"""
It is a good idea to keep any expressions used in an f-string as simple as possible. 
Packing in a bunch of complicated expressions into a string literal can result in 
code that is difficult to read and difficult to maintain.

"""


"""
f-strings are only available in Python version 3.6 and above. 
In earlier versions of Python, the .format() method can be used to get the
same results. 
"""
#print("{} has {} head and {} arms".format(human, head, arms))

"""
f-strings are shorter, and sometimes more readable, than using .format().
So they are more useful choice.
"""


"""
Note
There is also another way to print formatted strings: using the
% operator. Which you might see this in code that you find elsewhere,
and you can read about how it works here if you’re curious.
Keep in mind that this style has been phased out entirely in
Python 3. Just be aware that it exists and you may see it in
legacy Python code bases.
"""

####                Tasks               ####

# 1. Create a float object named weight with the value 0.2, and create
# a string object named animal with the value "newt". Then use these
# objects to print the following string using only string concatenation:
# 0.2 kg is the weight of the newt.

weight = 0.2
animal = "newt"
print(str(weight) + " kg " + "is the weight of the " + animal)

#2. Display the same string by using the .format() method and empty
# {} place-holders.

print("{} kg is the weight of the {}".format(weight, animal))

#3. Display the same string using an f-string.
print(f"{weight} kg is the weight of the {animal}")

##### End of Tasks


#####                   End of Streamline Print Statement                   #####
