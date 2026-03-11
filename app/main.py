def get_human_age(cat_age: int, dog_age: int) -> list:

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    if cat_age < 0 or dog_age < 0:
        raise ValueError

    return [convert_age(cat_age, 4), convert_age(dog_age, 5)]


def convert_age(age: int, const: int) -> int:
    if 14 < age < 24:
        result = 1
    elif age == 24:
        result = 2
    elif age > 24:
        result = 2 + (age - 24) // const
    else:
        result = 0
    return result
