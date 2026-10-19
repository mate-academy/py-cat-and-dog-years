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
        raise TypeError("cat_age and dog_age must be integers")

    def convert(age: int, years_per_extra_human_year: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // years_per_extra_human_year

    return [convert(cat_age, 4), convert(dog_age, 5)]
