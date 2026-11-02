def get_human_age(cat_age: int, dog_age: int) -> list[int]:
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
    """
    if (not isinstance(cat_age, int) or not isinstance(dog_age, int)
            or isinstance(cat_age, bool) or isinstance(dog_age, bool)):
        raise TypeError("Ages must be integers.")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative.")

    if cat_age < 15:
        human_cat_age = 0
    elif cat_age < 24:
        human_cat_age = 1
    else:
        human_cat_age = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        human_dog_age = 0
    elif dog_age < 24:
        human_dog_age = 1
    else:
        human_dog_age = 2 + (dog_age - 24) // 5

    return [human_cat_age, human_dog_age]
