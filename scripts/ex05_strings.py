# "Strings" are another data type in Python (along with numbers and boolean
# values which we've already seen)

# Strings are text data.

print("Strings can be in double quotes.")
print('Strings can also be in single quotes if you want.')
print("""If you enclose a string in a triple single quotes or triple double quotes,
it can span multiple lines.
You probably won't use this feature very often but it's a good thing to be aware of.
Sometimes you just want to put a really long string in your program without having to type
quotes at the beginning and end of every line.
""")

print("If you want a line break in your string, use the \n sequence.")

# Variables can hold strings.

my_string = "This is a string."

print(my_string)

# The len() function will tell us how long something is, and can be used on
# strings.

print("my_string is", len(my_string), "characters long.")

# The + operator works on strings by "adding" them together.

a_longer_string = my_string + " And so is this."

print(a_longer_string)

# When a variable contains a string, it is said to be a "string object" and has
# some nice features. For example, we can get an uppercase version of our
# string:

print(my_string.upper())

# We can do a find/replace as well:

print(my_string.replace("string", "really cool string object with lots of neat features"))
