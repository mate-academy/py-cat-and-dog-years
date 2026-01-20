def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Must be an integer")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Must be a positive age")

    return [convert_to_human(cat_age, 4), convert_to_human(dog_age, 5)]


def convert_to_human(age: int, div: int) -> int:
    if age >= 0 and age <= 15:
        return 0
    elif age > 15 and age < 24:
        return 1
    else:
        return 2 + (age - 24) // div
