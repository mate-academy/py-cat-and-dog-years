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
    pets_age = [cat_age, dog_age]
    converted_age = [0, 0]

    for i in range(len(pets_age)):
        if i == 0:
            if pets_age[i] >= 24:
                converted_age[i] = 2 + (pets_age[i] - 2) // 4
            elif pets_age[i] >= 15:
                converted_age[i] = 1
            else:
                converted_age[i] = 0

        if i == 1:
            if pets_age[i] >= 24:
                converted_age[i] = 2 + (pets_age[i] - 2) // 5
            elif pets_age[i] >= 15:
                converted_age[i] = 1
            else:
                converted_age[i] = 0

    return converted_age
