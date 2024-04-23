def get_human_age(cat_age: int | float, dog_age: int | float) -> list:
    if not (isinstance(cat_age, (int, float))
            and isinstance(dog_age, (int, float))):
        raise TypeError("Age should be a number")
    cat_to_human = convert_to_human(int(cat_age), 15, 9, 4)
    dog_to_human = convert_to_human(int(dog_age), 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(
        animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    if not 0 < animal_age < 50:
        raise ValueError("The data out of normal range")
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year
