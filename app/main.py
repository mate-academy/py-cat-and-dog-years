def _convert_to_human_age(animal_age: int, each_year: int) -> int:
    if animal_age < 15:
        return 0
    if animal_age < 24:
        return 1
    return 2 + (animal_age - 24) // each_year


def get_human_age(cat_age: int, dog_age: int) -> list:
    for age in (cat_age, dog_age):
        if isinstance(age, bool) or not isinstance(age, int):
            raise TypeError("cat_age and dog_age must be integers")
        if age < 0:
            raise ValueError("cat_age and dog_age can't be negative")

    return [
        _convert_to_human_age(cat_age, 4),
        _convert_to_human_age(dog_age, 5),
    ]
