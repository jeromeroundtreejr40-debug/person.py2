class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."

    def can_vote(self):
        return self.age >= 18
person_1 = Person("John", 17, "Canada")
person_2 = Person("Maria", 25, "Spain")

print(person_1)
print(person_2)

print(person_1.can_vote())
print(person_2.can_vote())
