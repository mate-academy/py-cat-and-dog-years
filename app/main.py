def convert_to_human(age: int, extra_rate: int) -> int:
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("Age must be an integer")
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // extra_rate


def get_human_age(cat_age: int, dog_age: int) -> list:
    return [
        convert_to_human(cat_age, 4),
        convert_to_human(dog_age, 5),
    ]
