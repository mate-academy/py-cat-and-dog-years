def _convert_to_human(animal_age: int, years_per_extra_human_year: int) -> int:
    first_period = 15
    second_period = 9

    if animal_age < first_period:
        return 0
    if animal_age < first_period + second_period:
        return 1
    extra_years = animal_age - first_period - second_period
    return 2 + extra_years // years_per_extra_human_year


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
    return [
        _convert_to_human(cat_age, 4),
        _convert_to_human(dog_age, 5),
    ]
