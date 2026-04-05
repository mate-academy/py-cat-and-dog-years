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

    cat_human_age = 0
    dog_human_age = 0

    cat_ages = [15, 24]
    cat_ages.extend(list(range(28, cat_age + 1, 4)))
    for age in cat_ages:
        if cat_age >= age:
            cat_human_age += 1

    dog_ages = [15, 24]
    dog_ages.extend(list(range(29, dog_age + 1, 5)))
    for age in dog_ages:
        if dog_age >= age:
            dog_human_age += 1

    return [cat_human_age, dog_human_age]
