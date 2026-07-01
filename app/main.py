def calculate_age(pet_age: int, step: int) -> int:
    if pet_age < 15:
        human_age = 0
    elif 15 <= pet_age <= 23:
        human_age = 1
    else:
        pet_age -= 24
        human_age = (pet_age // step) + 2
    return human_age


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
    # TODO: Implement this function
    return [calculate_age(cat_age, 4), calculate_age(dog_age, 5)]
