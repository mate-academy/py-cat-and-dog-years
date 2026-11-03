def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    return [
        convert_age(cat_age, 4),
        convert_age(dog_age, 5),
    ]


def convert_age(animal_age: int, step: int) -> int:
    if animal_age < 15:
        return 0
    if animal_age < 24:
        return 1
    return 2 + (animal_age - 24) // step
