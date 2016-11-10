# Another commonly used data type in Python is the dictionary. Dictionaries map
# one value to another.

# Create dictionaries with the dict() function:

my_dict = dict()

# We add items to the dictionary by assigning "keys" to "values".
my_dict['dog'] = 'Rex' # key = 'dog', value = 'Rex'
my_dict['cat'] = 'Snowball'
my_dict['velociraptor'] = 'Fluffy'

# Just like with lists, there's an easy to use "literal" syntax for creating
# dictionaries:

my_dict = {
    'dog': 'Rex', # key = 'dog', value = 'Rex'
    'cat': 'Snowball',
    'velociraptor': 'Fluffy',
}

# Note that when we print out a dictionary, we won't necessarily get the items
# back in the order we created them!
print(my_dict)

# Dictionaries are "unordered"! That means that Python makes no promises about
# the order in which items are returned when we iterate over them. There is a
# special kind of dictionary in the collections module called an OrderedDict
# that you can use if you need to iterate over the keys in a dictionary in a
# guaranteed order.

# Access a value in a dictionary by looking it up with the appropriate key:
print("The name of the dog is", my_dict['dog'])

# We can use the "in" operator with dictionaries. It will tell us whether a
# dictionary contains a specific key:
print('dog' in my_dict) # True!
print('Rex' in my_dict) # False! "in" looks at the *keys* of a dictionary, not the values!

# Handy trick: if you have two lists, you can use the dict() and zip()
# functions to create a dictionary, where one list is the keys and the other
# list is the values!

species = ['sheep', 'goat', 'llama']
names = ['Sally', 'Gary', 'Larry']

another_dict = dict(zip(species, names))
print("The goat's name is", another_dict['goat'])
