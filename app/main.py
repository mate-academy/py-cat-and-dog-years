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
    ages = [0, 0]
    if (not isinstance(cat_age, int) or not isinstance(dog_age, int)):
        raise TypeError()

    for index, age in enumerate([cat_age, dog_age]):
        if age < 15:
            ages[index] = 0
        elif age < 24:
            ages[index] = age // 15
        elif age == 24:
            ages[index] = 2
        else:
            if index == 0:
                ages[index] = (cat_age - 24) // 4 + 2
            else:
                ages[index] = (dog_age - 24) // 5 + 2
    return ages
