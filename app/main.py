def convert_age(age: int, step: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // step


def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")
    return [convert_age(cat_age, 4), convert_age(dog_age, 5)]
