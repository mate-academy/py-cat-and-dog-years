def animal_age_to_human_age(animal_age: int, years_per_human: int) -> int:
    if not isinstance(animal_age, int):
        raise TypeError("Age must be an int")

    if animal_age < 15:
        return 0
    if animal_age < 24:
        return 1
    return 2 + (animal_age - 24) // years_per_human


def cat_age_to_human_age(cat_age: int) -> int:
    return animal_age_to_human_age(cat_age, years_per_human=4)


def dog_age_to_human_age(dog_age: int) -> int:
    return animal_age_to_human_age(dog_age, years_per_human=5)


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be ints")

    return [
        cat_age_to_human_age(cat_age),
        dog_age_to_human_age(dog_age),
    ]
