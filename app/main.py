class AgeError(ValueError):
    pass


def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.
    Cat and dog ages should be in range from 0 to 150

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

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Cat and dog age must be non-negative")

    if cat_age > 150 or dog_age > 150:
        raise AgeError(
            "Cats and dogs don't live that long. Like people, unfortunately..."
        )

    cat_human_age = 0
    dog_human_age = 0

    if cat_age > 23:
        cat_human_age = (cat_age - 16) // 4
    elif cat_age > 14:
        cat_human_age = 1

    if dog_age > 23:
        dog_human_age = (dog_age - 14) // 5
    elif dog_age > 14:
        dog_human_age = 1

    return [cat_human_age, dog_human_age]
