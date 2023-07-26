class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population


if __name__ == '__main__':
    """
        In this example, we define a Person class with a population attribute 
        and an __init__ method that increments the population attribute every time 
        a new Person object is created.
        
        Reference:
            https://medium.com/@mkuhikar/python-decorators-advanced-67420a5b7278
    """
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)

    print(Person.get_population())  # Output: 2
