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
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    def calculate_age(animal_age: int, years_per_human_year: int) -> int:
        if animal_age < 15:
            return 0
        elif animal_age < 24:
            return 1
        else:
            return 2 + (animal_age - 24) // years_per_human_year

    cat_human_age = calculate_age(cat_age, 4)

    dog_human_age = calculate_age(dog_age, 5)

    return [cat_human_age, dog_human_age]
