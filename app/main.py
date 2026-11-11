def convert_to_human_age(
        animal_age: int,
        first_period: int,
        second_period: int,
        each_next_period: int
) -> int:
    if animal_age < first_period:
        return 0
    if animal_age < first_period + second_period:
        return 1
    return 2 + (animal_age - first_period - second_period) // each_next_period


def get_human_age(cat_age: int, dog_age: int) -> list:
    return [
        convert_to_human_age(cat_age, 15, 9, 4),
        convert_to_human_age(dog_age, 15, 9, 5),
    ]
