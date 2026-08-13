FIRST_PERIOD = 15
SECOND_PERIOD = 9
CAT_EXTRA_PERIOD = 4
DOG_EXTRA_PERIOD = 5


def convert_to_human_age(animal_age: int, extra_period: int) -> int:
    if animal_age < FIRST_PERIOD:
        return 0
    if animal_age < FIRST_PERIOD + SECOND_PERIOD:
        return 1
    rest = animal_age - FIRST_PERIOD - SECOND_PERIOD
    return 2 + rest // extra_period


def get_human_age(cat_age: int, dog_age: int) -> list:
    return [
        convert_to_human_age(cat_age, CAT_EXTRA_PERIOD),
        convert_to_human_age(dog_age, DOG_EXTRA_PERIOD),
    ]
