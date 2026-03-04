def get_human_age(cat_age: int, dog_age: int) -> list:

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age must be non-negative")

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be an integer")

    return [age_converter(cat_age, 4), age_converter(dog_age, 5)]


def age_converter(age: int, step: int) -> int:
    animal_age = age
    res = 0
    if 14 < animal_age < 24:
        res += 1
    elif animal_age >= 24:
        res += (2 + (age - 24) // step)

    return res
