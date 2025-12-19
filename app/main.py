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
    human_age = [0, 0]

    if cat_age < 15:
        human_age[0] = 0
    elif cat_age < 24:
        human_age[0] = 1
    else:
        variable = cat_age - 23
        if variable % 4 == 0:
            variable -= 1
        human_age[0] = (variable // 4) + 2

    if dog_age < 15:
        human_age[1] = 0
    elif dog_age < 24:
        human_age[1] = 1
    else:
        variable = dog_age - 23
        if variable % 5 == 0:
            variable -= 1
        human_age[1] = (variable // 5) + 2
    return human_age
