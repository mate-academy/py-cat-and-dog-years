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

    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Ages must be integers")

    cat = 0
    dog = 0

    if cat_age >= 15 and cat_age <= 23:
        cat = 1
    elif cat_age >= 24 and cat_age <= 27:
        cat = 2
    elif cat_age >= 28:
        cat_age -= 28
        cat += (cat_age // 4) + 3

    if dog_age >= 15 and dog_age <= 23:
        dog = 1
    elif dog_age >= 24 and dog_age <= 28:
        dog = 2
    elif dog_age >= 29:
        dog_age -= 29
        dog += (dog_age // 5) + 3

    return [cat, dog]
