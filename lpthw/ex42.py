# Animal is-a object (yes, sort	of confusing) look at the extra	credit
class Animal(object):
    pass

# dog is-a animal
class Dog(Animal):
    def __init__(self,name):
        # dog has-a name
        self.name = name

# cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        # cat has-a name
        self.name = name

# person is-a object
class Person(object):
    def __init__(self, name):
        # person has-a name
        self.name = name
        # person has a pet of some kind
        self.pet = None

# employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        # what sorcery is this
        super(Employee, self).__init__(name)
        # employee has-a salary

# fish is-a object
class Fish(object):
    pass

# salmon is-a fish
class Salmon(Fish):
    pass

# halibut is-a fish
class Halibut(Fish):
    pass

# rover is-a dog
rover = Dog('rover')

# satan is-a cat
satan = Cat('satan')

# mary is-a person
mary = Person('mary')

# 'mary' is-a person and has-a pet 'satan'
mary.pet = satan

#  employee 'frank' is-a person, has-a name 'frank' and salary '120000'
frank = Employee('Frank', 120000)

# employee frank is-a person and has-a pet 'rover'
frank.pet = rover

# flipper is-a instance/object of fish
flipper = Fish()

# crouse is-a instance/object of salmon
crouse = Salmon()

# harry is-a instance/object of halibut
harry = Halibut()
