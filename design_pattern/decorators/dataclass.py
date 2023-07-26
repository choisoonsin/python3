from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    email: str = ""  # default value


if __name__ == '__main__':
    """
        the dataclass decorator provides a string representation of the object
        (__repr__) 
        
        Reference:
            https://medium.com/@mkuhikar/python-decorators-advanced-67420a5b7278
    """
    person1 = Person('choi', 30)

    print(person1)
