def get_human_age(cat_age: int, dog_age: int) -> list[int, int]:
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
    result = [0, 0]

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age >= 15:
        cat_age -= 15
        result[0] += 1
        if cat_age >= 9:
            cat_age -= 9
            result[0] += 1
            result[0] += cat_age // 4
    if dog_age >= 15:
        dog_age -= 15
        result[1] += 1
        if dog_age >= 9:
            dog_age -= 9
            result[1] += 1
            result[1] += dog_age // 5
    return result
