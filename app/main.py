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

    if isinstance(cat_age, int) is False:
        raise ValueError("Type Value Error")
    if isinstance(dog_age, int) is False:
        raise ValueError("Type Value Error")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Negative Value Error")

    cat_man_year = (cat_age >= 15) + (cat_age >= 24) + (cat_age >= 28) * \
                   (((cat_age - 28) // 4) + 1)
    dog_man_year = (dog_age >= 15) + (dog_age >= 24) + (dog_age >= 29) * \
                   (((dog_age - 29) // 5) + 1)
    return [cat_man_year, dog_man_year]
