def get_human_age(cat_age: int, dog_age: int) -> list:
    validate_age(cat_age)
    validate_age(dog_age)
    return [convert_cat_age(cat_age), convert_dog_age(dog_age)]


def validate_age(age: int) -> None:
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError(f"Age must be an integer, got {type(age)}")

    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")


def convert_cat_age(age: int) -> int:
    if age < 15:
        return 0

    if age < 24:
        return 1

    return 2 + (age - 24) // 4


def convert_dog_age(age: int) -> int:
    if age < 15:
        return 0

    if age < 24:
        return 1

    return 2 + (age - 24) // 5
