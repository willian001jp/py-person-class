class Person:
    people = {}  # Class attribute to store instances by name

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self  # Add instance to people dict


def create_person_list(people: list) -> list:
    # First pass: create all Person instances
    for person_data in people:
        Person(person_data["name"], person_data["age"])

    # Second pass: establish relationships
    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            person.wife = Person.people[wife_name]

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            person.husband = Person.people[husband_name]

    return list(Person.people.values())
