FIRST_HUMAN_YEAR_THRESHOLD = 15
SECOND_HUMAN_YEAR_THRESHOLD = 24


def calc_age(animal_age: int, step: int) -> int:
    if animal_age < FIRST_HUMAN_YEAR_THRESHOLD:
        return 0

    if animal_age < SECOND_HUMAN_YEAR_THRESHOLD:
        return 1

    if animal_age < SECOND_HUMAN_YEAR_THRESHOLD + step:
        return 2

    return 2 + (animal_age - SECOND_HUMAN_YEAR_THRESHOLD) // step


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
    # TODO: Implement this function
    # Write your tests first, then implement the logic
    return [0, 0]
    if not (
            isinstance(cat_age, int) and isinstance(dog_age, int)
    ):
        raise AttributeError("Incorrect value - not a number - for the age")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Incorrect value - negative - for the age")

    return [
        calc_age(cat_age, 4),
        calc_age(dog_age, 5)
    ]
