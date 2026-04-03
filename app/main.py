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

    def cat_to_human(age: int) -> int:
        if age < 15:
            return 0
        human_years = 1
        if age >= 24:
            human_years += 1
            age -= 24
            human_years += age // 4
        return human_years

    def dog_to_human(age: int) -> int:
        if age < 15:
            return 0
        human_years = 1
        if age >= 24:
            human_years += 1
            age -= 24
            human_years += age // 5
        return human_years

    return [cat_to_human(cat_age), dog_to_human(dog_age)]
