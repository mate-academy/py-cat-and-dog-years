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

    if not (isinstance(cat_age, int) and isinstance(dog_age, int)):
        raise TypeError
    if cat_age < 0 or dog_age < 0:
        raise ValueError

    def convert(age: int, step: int) -> int:
        animal_years = 0
        if age >= 15:
            animal_years += 1
            age -= 15
            if age >= 9:
                animal_years += 1
                age -= 9
                if age >= step:
                    animal_years += age // step
        return animal_years

    result = [convert(cat_age, 4), convert(dog_age, 5)]

    return result
