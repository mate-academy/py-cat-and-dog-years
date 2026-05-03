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

    Examples:
        get_human_age(0, 0) == [0, 0]
        get_human_age(15, 15) == [1, 1]
        get_human_age(24, 24) == [2, 2]
    """
    if type(cat_age) is not int:
        raise TypeError("cat_age must be int")
    if type(dog_age) is not int:
        raise TypeError("dog_age must be int")

    return [
        _years_to_human(cat_age, extra_period=4),
        _years_to_human(dog_age, extra_period=5),
    ]


def _years_to_human(animal_age: int, extra_period: int) -> int:
    if animal_age < 15:
        return 0
    if animal_age < 24:
        return 1
    return 2 + (animal_age - 24) // extra_period
