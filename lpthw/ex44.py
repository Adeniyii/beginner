"""CLASS INHERITANCE"""

# created a parent base-class
class Parent(object):
    def override(self):
        print("Parent override()")

    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("parent altered()")


# A child sub-class to inherit functionality of the parent base-class
class Child(Parent):
    # To override the override() function inherited from the parent base-class
    def override(self):
        print("child override()")
        # To call back the override() function inherited from the parent base-class.
        super(Child, self).override()

    def altered(self):
        # To override the altered() function from the parent base-class
        print("child altered()")
        # To call back the overridden altered() function from the parent base-class.
        super(Child, self).altered()
        # To override the altered() function from the parent base-class
        print("child altered()")


dad = Parent()
son = Child()

print()
dad.implicit()
son.implicit()
print()
dad.override()
son.override()
print()
dad.altered()
son.altered()
print()

"""USING SUPER() WITH __INIT__"""

# create Daddy() base-class
class Daddy(object):
    # create init functionality
    def __init__(self):
        self.gandoki = 'gandoki'
        self.prime = True
        print(f"I am {self.gandoki}. it is {self.prime}.")

# create Sonny() sub-class and inherit functionality from Daddy() base-class
class Sonny(Daddy):
    # To override init functionality gotten from Daddy() base-class
    def __init__(self):
        self.user = 'Shackamanfinus'
        print(f"No teletubbies for you shir {self.user}.")
        # To restore init functionality gotten from Daddy() base-class.
        super(Sonny, self).__init__()


dada = Daddy()
bubu = Sonny()
print()

"""CLASS COMPOSITION"""

class Other(object):
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()

    def override(self):
        print("CHILD override()")
    def implicit(self):
        self.other.implicit()
    def altered(self):
        print("BEFORE altered()")
        self.other.altered()
        print("AFTER altered()")


ac = Child()
ac.override()
ac.implicit()
ac.altered()
