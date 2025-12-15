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

    Raises:
        TypeError: If cat_age or dog_age are not integers
    """
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Both cat_age and dog_age must be integers")

    if isinstance(cat_age, bool) or isinstance(dog_age, bool):
        raise TypeError("Both cat_age and dog_age must be integers")

    cat_age = max(0, cat_age)
    dog_age = max(0, dog_age)

    def convert_cat_years(age: int) -> int:
        """Convert cat years to human years."""
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // 4

    def convert_dog_years(age: int) -> int:
        """Convert dog years to human years."""
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // 5

    return [convert_cat_years(cat_age), convert_dog_years(dog_age)]
