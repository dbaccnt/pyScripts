from collections import Counter


class1 = ["Bob","James","Chad","Darcy","Penny","Hannah",
          "Kevin","James","Melanie","Becky","Steve","Frank"]

class2 = ["Bill","Barry","Cindy","Debbie","Frank","Gabby",
          "Gabby","Kelly","James","Joe","Sam","Tara","Ziggy"]

# TODO: Create a counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)

# TODO: How many students in class 1 named James?
print(c1["James"])

# TODO: How many students are in class 1?
print(sum(c1.values()), "Students in class 1")
print(sum(c2.values()), "Students in class 2")

# TODO: Combine the two classes
c1.update(class2)
print(sum(c1.values()), "Students in class 1")

# TODO: Whats the most common name in the two classes (3) most common name in both clases
print(c1.most_common(3))

# TODO: Separate the classes again
c1.subtract(class2)
print(c1.most_common(1))


# TODO: Whats the common between the two classes
print(c1 & c2) # the & does an intersection operation between the 2 dictionary arrays