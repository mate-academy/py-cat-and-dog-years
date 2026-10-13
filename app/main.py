def _calculate_human_age(animal_age: int, years_per_human_year: int) -> int:
    if animal_age < 15:
        return 0
    elif animal_age < 24:
        return 1
    return 2 + (animal_age - 24) // years_per_human_year


def get_cat_human_age(cat_age: int) -> int:
    return _calculate_human_age(cat_age, years_per_human_year=4)


def get_dog_human_age(dog_age: int) -> int:
    return _calculate_human_age(dog_age, years_per_human_year=5)


def get_human_age(cat_age: int, dog_age: int) -> list:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Both cat_age and dog_age must be integers")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Both cat_age and dog_age must be non-negative")
    return [get_cat_human_age(cat_age), get_dog_human_age(dog_age)]
