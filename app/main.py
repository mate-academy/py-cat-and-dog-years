def get_human_age(cat_age: int = 0, dog_age: int = 0) -> list:
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

    Examples:
        get_human_age(0, 0) == [0, 0]
        get_human_age(15, 15) == [1, 1]
        get_human_age(24, 24) == [2, 2]
    """
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be int")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age must be positive")
    return [convert_to_human(cat_age, 4), convert_to_human(dog_age, 5)]


def convert_to_human(age: int, sep: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // sep
