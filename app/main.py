def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.

    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1.
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1.

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

    def _convert_age(
        age: int,
        first_threshold: int,
        second_threshold: int,
        extra_rate: int,
    ) -> int:
        if age < first_threshold:
            return 0

        human_years = 1
        remaining = age - first_threshold

        if remaining < second_threshold:
            return human_years

        human_years += 1
        remaining -= second_threshold
        human_years += remaining // extra_rate
        return human_years

    cat_human_age = _convert_age(
        cat_age,
        first_threshold=15,
        second_threshold=9,
        extra_rate=4,
    )
    dog_human_age = _convert_age(
        dog_age,
        first_threshold=15,
        second_threshold=9,
        extra_rate=5,
    )
    return [cat_human_age, dog_human_age]
