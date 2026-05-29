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
    # Write your tests first, then implement the logic
    cat_age_human = 0
    dog_age_human = 0
    reste_age = 0
    liste_convert_age = []

    if (not isinstance(cat_age, int) or not isinstance(dog_age, int)):
        raise TypeError
    if (cat_age < 0 or dog_age < 0):
        raise ValueError

    if cat_age >= 15:
        reste_age = cat_age - 15
        cat_age_human += 1
        if reste_age >= 9:
            reste_age -= 9
            cat_age_human += (1 + reste_age // 4)
        else:
            pass
    else:
        cat_age_human = 0

    if dog_age >= 15:
        reste_age = dog_age - 15
        dog_age_human += 1
        if reste_age >= 9:
            reste_age -= 9
            dog_age_human += (1 + reste_age // 5)
    else:
        dog_age_human = 0

    liste_convert_age.append(cat_age_human)
    liste_convert_age.append(dog_age_human)

    return liste_convert_age
