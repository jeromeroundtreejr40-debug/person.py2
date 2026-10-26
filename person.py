class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."

    def can_vote(self):
        return self.age >= 18
