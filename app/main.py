def convert_to_human(age: float) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    if age < 28:
        return 2
    if age < 32:
        return 3
    return 4


def get_human_age(cat_age: float, dog_age: float) -> tuple[int, int]:
    return convert_to_human(cat_age), convert_to_human(dog_age)
