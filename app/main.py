def convert_age(age: int, first: int, second: int, step: int) -> int:
    if age < first:
        return 0
    if age < first + second:
        return 1
    return 2 + (age - first - second) // step


def get_human_age(cat_age: int, dog_age: int) -> list:
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
        raise TypeError("Ages must be integers.")
    return [
        convert_age(cat_age, first=15, second=9, step=4),
        convert_age(dog_age, first=15, second=9, step=5),
    ]
