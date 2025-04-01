class Person:
    people = {}  # Class attribute to store instances by name

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self  # Add instance to people dict


def create_person_list(people: list) -> list:
    # Create all Person instances using list comprehension
    [Person(person_data["name"], person_data["age"]) for person_data in people]

    # Establish relationships
    for person_data in people:
        person = Person.people[person_data["name"]]
        person.wife = Person.people.get(person_data.get("wife"))
        person.husband = Person.people.get(person_data.get("husband"))

    return list(Person.people.values())
