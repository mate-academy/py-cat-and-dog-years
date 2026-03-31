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

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Incorrect input datatypes - ensure they are integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Negative input values received - ensure they >= 0")

    if cat_age > 100 or dog_age > 100:
        raise ValueError("Large input values received - ensure they <= 100")

    human_cat_age = 0
    human_dog_age = 0

    if cat_age >= 15:
        human_cat_age += 1

    if cat_age >= 24:
        human_cat_age += 1
        human_cat_age += (cat_age - 24) // 4

    if dog_age >= 15:
        human_dog_age += 1

    if dog_age >= 24:
        human_dog_age += 1
        human_dog_age += (dog_age - 24) // 5

    return [human_cat_age, human_dog_age]
