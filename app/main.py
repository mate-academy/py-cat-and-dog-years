def get_humane_age_by_intervals(intervals: list, animal_age: int) -> int:
    human_age = 0
    left_age = animal_age

    for current_int in intervals:
        left_age -= current_int
        if left_age >= 0:
            human_age += 1
        else:
            break

    if left_age > 0:
        human_age += left_age // intervals[-1]

    return human_age


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

    Raises:
        TypeError: if cat_age or dog_age is not an int (bool is rejected too).
        ValueError: if cat_age or dog_age is negative.

    Examples:
        get_human_age(0, 0) == [0, 0]
        get_human_age(15, 15) == [1, 1]
        get_human_age(24, 24) == [2, 2]
    """
    for name, age in (("cat_age", cat_age), ("dog_age", dog_age)):
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError(
                f"{name} must be an integer, got {type(age).__name__}"
            )
        if age < 0:
            raise ValueError(f"{name} cannot be negative, got {age}")

    cat_interval = [15, 9, 4]
    dog_interval = [15, 9, 5]

    return [get_humane_age_by_intervals(cat_interval, cat_age),
            get_humane_age_by_intervals(dog_interval, dog_age)]
