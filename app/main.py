def animal_to_human(age: int, first: int, second: int, step: int) -> int:
    if age < first:
        return 0
    if age < first + second:
        return 1
    return int(2 + (age - first - second) // step)


def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages must be non-negative")

    return [
        animal_to_human(cat_age, first=15, second=9, step=4),
        animal_to_human(dog_age, first=15, second=9, step=5),
    ]
