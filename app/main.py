def get_human_age(cat_age: int, dog_age: int) -> list:
    if (isinstance(cat_age, int) and isinstance(dog_age, int)
            and cat_age > 0 and dog_age > 0):
        cat_to_human = convert_to_human(cat_age, 15, 9, 4)
        dog_to_human = convert_to_human(dog_age, 15, 9, 5)
        return [cat_to_human, dog_to_human]
    else:
        raise ValueError("Animal age should be positive integer")


def convert_to_human(
        animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year
