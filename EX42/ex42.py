## Animal is-a object
class Animal(object):
    pass

## Dog is-an animal
class Dog(Animal):

    def __init__(self, name):
        ## Class Dog has-a name named name
        self.name = name

## Cat is-an Animal
class Cat(Animal):

    def __init__(self, name):
        ## Class Cat has-a name named name
        self.name = name

## Person is-an object
class Person(object):

    def __init__(self.name):
        ## Person has-a name named name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = none

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## diu mud 9 lei ga
        super(Employee, self).__init__(name)
        ## Employee has-a salary named salary


##Fish is-an object
class Fish(object):
    pass

##Salmon is-a Fish
class Salmon(Fish):
    pass

##Halibut is-a Fish
class Halibut(Fish):
    pass


##rover is-a Dog
rover = Dog("Rover")

##satan is-a cat
satan = Cat("Satan")

##mary is-a Person
mary = Person("Mary")

##mary has-a pet named satan
mary.pet = satan

##frank is-an Employee
frank = Employee("Frank", 120000)

##frank has-a pet named rover
frank.pet = rover

##flipper is-a fish
flipper = fish()

##crouse is-a Salmon
crouse = Salmon()

##harry is-a Halibut
harry = Halibut()
