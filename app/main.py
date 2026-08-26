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
    if type(cat_age) != int or type(dog_age) != int:
        raise TypeError("cat_age and dog_age must be of type int")
    if not 0 <= cat_age <= 100 or not 0 <= dog_age <= 100:
        raise ValueError("cat_age and dog_age must be between 0 and 100")
    result = []

    def two_years(age: int) -> int:
        if age < 15:
            return 0
        if 15 <= age < 24:
            return 1
        return 2
    if cat_age > 24:
        result.append(two_years(cat_age) + (cat_age - 24) // 4)
    else:
        result.append(two_years(cat_age))
    if dog_age > 24:
        result.append(two_years(dog_age) + (dog_age - 24) // 5)
    else:
        result.append(two_years(dog_age))
    return result
