from collections import defaultdict

fruits = ['apple','pear','orange','banana','apple','grape','banana','banana']

# factory function essentially acts as the creator of whatever the default value is
fruitcounter = defaultdict(int)

# TODO: count the elements in the list
for fruit in fruits:
    fruitcounter[fruit] += 1

# TODO: print the result
print(fruitcounter)

