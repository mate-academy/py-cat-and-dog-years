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
    return [cat_year_converting(cat_age), dog_year_converting(dog_age)]


def cat_year_converting(cat_age: int) -> int:
    human_age = 0
    if not isinstance(cat_age, int):
        raise TypeError("cat age must be an integer")

    if cat_age < 0:
        raise ValueError("cat's age must be >= 0")
    elif cat_age < 15:
        return human_age
    elif 15 <= cat_age < 24:
        human_age = 1
        return human_age
    else:
        human_age = 2 + (cat_age - 24) // 4
        return human_age


def dog_year_converting(dog_age: int) -> int:
    human_age = 0
    if not isinstance(dog_age, int):
        raise TypeError("dog age must be an integer")

    if dog_age < 0:
        raise ValueError("dog's age must be >= 0")
    elif dog_age < 15:
        return human_age
    elif 15 <= dog_age < 24:
        human_age = 1
        return human_age
    else:
        human_age = 2 + (dog_age - 24) // 5
        return human_age
