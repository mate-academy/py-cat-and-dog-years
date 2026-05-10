def get_age(age: int | str, divider: int) -> int:
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0:
        raise ValueError("age must be >= 0")
    result = 0
    if age // 15:
        result += 1
        age -= 15
    else:
        return result
    if age // 9:
        result += 1
        age -= 9
    else:
        return result
    while age // divider:
        result += 1
        age -= divider
    return result


def get_human_age(cat_age: int | str, dog_age: int | str) -> list[int]:
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
    cat_human_age = get_age(cat_age, 4)
    dog_human_age = get_age(dog_age, 5)
    return [cat_human_age, dog_human_age]
