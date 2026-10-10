def convert_age(age: int, step: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // step


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """
    Convert cat and dog ages to human years.

    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1

    Args:
        cat_age: Cat's age in cat years
        dog_age: Dog's age in dog years

    Returns:
        List with [cat_human_age, dog_human_age]

    Raises:
        TypeError: if any age is not an integer
    """
    for age in (cat_age, dog_age):
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError("Age must be an integer")
    return [convert_age(cat_age, 4), convert_age(dog_age, 5)]
