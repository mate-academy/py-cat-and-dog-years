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

    def convert_human_age(age: int, interval: int) -> int:
        if isinstance(age, bool) or not isinstance(age, int):
            raise TypeError("cat_age and dog_age must be integers")
        if age < 0:
            raise ValueError("cat_age and dog_age must be non-negative")
        if age < 15:
            return 0

        if age < 24:
            return 1

        human_age = 2
        age -= 24

        if age <= 0:
            return human_age

        return human_age + (age // interval)

    return [convert_human_age(cat_age, 4), convert_human_age(dog_age, 5)]
