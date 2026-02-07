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

    def count_animail_age(age: int, age_div: int) -> int:
        if age < 0:
            raise ValueError("Age cannot be negative.")

        if not isinstance(age, int):
            raise TypeError("Age need to be a number")

        if age >= 1_000_000:
            raise ValueError("Age is unrealistically large")

        animal_age = 0
        if age >= 24:
            animal_age += 2
            animal_age += (age - 24) // age_div
        elif age >= 15:
            animal_age = 1
        return animal_age

    return [
        count_animail_age(age, age_div)
        for age, age_div in [[cat_age, 4], [dog_age, 5]]
    ]
