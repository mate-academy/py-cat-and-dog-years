MAX_CAT_AGE = 38    # Oldest recorded cat
MAX_DOG_AGE = 29    # Oldest recorded dog


def convert_age(age: int, step: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // step


def check_age(age: int, max_age: int) -> None:
    if not isinstance(age, int):
        raise TypeError("Age should be an integer.")
    if age > max_age:
        raise ValueError("Unrealistic age value.")
    if age < 0:
        raise ValueError("Age value should be positive.")
    if age == 0:
        raise ValueError("Age value should be greater than 0.")


def get_human_age(cat_age: int, dog_age: int) -> list:
    check_age(cat_age, MAX_CAT_AGE)
    check_age(dog_age, MAX_DOG_AGE)
    return [convert_age(cat_age, 4), convert_age(dog_age, 5)]
