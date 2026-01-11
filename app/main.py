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
    if not isinstance(cat_age, int):
        raise TypeError('The value of "cat_age" should be int')
    if not isinstance(dog_age, int):
        raise TypeError('The value of "dog_age" should be int')
    if cat_age < 0 or dog_age < 0:
        raise ValueError("The values should be greater than 0")
    cat_human_age = 0
    dog_human_age = 0

    if cat_age >= 15:
        cat_age -= 15
        cat_human_age += 1
        if cat_age >= 9:
            cat_age -= 9
            cat_human_age += 1
            cat_human_age += cat_age // 4
    if dog_age >= 15:
        dog_age -= 15
        dog_human_age += 1
        if dog_age >= 9:
            dog_age -= 9
            dog_human_age += 1
            dog_human_age += dog_age // 5

    return [cat_human_age, dog_human_age]
