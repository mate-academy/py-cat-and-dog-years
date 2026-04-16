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

    def convert_cat_years(cat_age: int) -> int:
        if cat_age < 15:
            return 0
        elif cat_age < 24:  # 15 + 9
            return 1
        else:
            return 1 + 1 + (cat_age - 24) // 4

    def convert_dog_years(dog_age: int) -> int:
        if dog_age < 15:
            return 0
        elif dog_age < 24:
            return 1
        else:
            return 1 + 1 + (dog_age - 24) // 5

    return [convert_cat_years(cat_age), convert_dog_years(dog_age)]
