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
    if (
            not isinstance(cat_age, (int, float))
            or not isinstance(dog_age, (int, float))
            or isinstance(cat_age, bool)
            or isinstance(dog_age, bool)
    ):
        raise TypeError
    if cat_age < 0 or cat_age >= 101 or dog_age < 0 or dog_age >= 101:
        raise ValueError
    result = []
    for age in (cat_age, dog_age):
        if age < 15:
            human_age = 0
        elif 15 <= age < 24:
            human_age = 1
        else:
            age -= 24
            human_age = 2 + (age // 4 if len(result) == 0 else age // 5)
        result.append(human_age)
    return result
