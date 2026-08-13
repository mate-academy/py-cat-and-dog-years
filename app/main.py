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
    first_year = 15
    second_year = 9
    cat_following_year = 4
    dog_following_year = 5

    if cat_age < first_year:
        cat_human_age = 0
    elif cat_age < first_year + second_year:
        cat_human_age = 1
    else:
        cat_human_age = (2
                         + (cat_age - first_year - second_year)
                         // cat_following_year
                         )

    if dog_age < first_year:
        dog_human_age = 0
    elif dog_age < first_year + second_year:
        dog_human_age = 1
    else:
        dog_human_age = (2
                         + (dog_age - first_year - second_year)
                         // dog_following_year
                         )

    return [cat_human_age, dog_human_age]
