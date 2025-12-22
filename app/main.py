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
    # Write your tests first, then implement the logic
    animal_ages = [cat_age, dog_age]
    human_ages = [0, 0]
    for i, age in enumerate(animal_ages):
        if age < 15:
            human_ages[i] = 0
        elif 15 <= age < 24:
            human_ages[i] = 1
    if animal_ages[0] >= 24:
        human_ages[0] = 2 + (animal_ages[0] - 24) // 4
    if animal_ages[1] >= 24:
        human_ages[1] = 2 + (animal_ages[1] - 24) // 5
    return human_ages
