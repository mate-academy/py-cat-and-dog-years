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
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be an integer")

    return [
        convert_age_to_human_years(cat_age, 4),
        convert_age_to_human_years(dog_age, 5)
    ]


def convert_age_to_human_years(
        age: int,
        extra_years_step: int,
) -> int:

    if age < 15:
        return 0

    elif age < 24:
        return 1

    else:
        return 2 + (age - 24) // extra_years_step
