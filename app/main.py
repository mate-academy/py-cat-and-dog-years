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
    human_age = []

    cat_human_age = 0
    if cat_age >= 15:
        cat_human_age = 1
    if cat_age >= 24:
        cat_human_age = 2 + (cat_age - 24) // 4

    dog_human_age = 0
    if dog_age >= 15:
        dog_human_age = 1
    if dog_age >= 24:
        dog_human_age = 2 + (dog_age - 24) // 5

    human_age.append(cat_human_age)
    human_age.append(dog_human_age)

    return human_age
