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
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError
    if cat_age < 0 or dog_age < 0:
        raise ValueError

    cat_human_age = 0
    dog_human_age = 0
    animal_age_array = [cat_age, dog_age]
    human_age_array = [cat_human_age, dog_human_age]

    for i, age in enumerate(animal_age_array):
        if 15 <= age < 24:
            human_age_array[i] = 1
        elif age == 24:
            human_age_array[i] = 2
        elif age > 24 and i == 0:
            human_age_array[i] = 2 + int((age - 24) / 4)
        elif age > 24 and i == 1:
            human_age_array[i] = 2 + int((age - 24) / 5)

    return human_age_array
