def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Arguments must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")

    return [convert_to_human(cat_age, 4), convert_to_human(dog_age, 5)]


def convert_to_human(age: int, divisor: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // divisor
