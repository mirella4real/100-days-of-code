my_list_of_things = ['thing 1', 'thing 2', 'thing 3', 'more things', 'all the things']

# looping throug lists
print('This is my list of things\n')
for thing in my_list_of_things:
    print('\t' + thing.title())

# using range()
print('\nTo make a list of numbers, use range():\n')
my_list_of_numbers = list(range(1,6))
print(my_list_of_numbers)

print('\nThen combine math with range():\n')
my_list_of_squares = []
for value in range(1, 6):
    my_list_of_squares.append(value**2)

print(my_list_of_squares)

# loop through a slice of the list
print('\nLooping through lists using slices:\n')
for t in my_list_of_things[:2]:
    print('\t' + t.title() + " was in a Dr. Seus book")

