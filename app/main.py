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
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError
    if cat_age < 0 or dog_age < 0:
        raise ValueError

    if cat_age <= 14:
        cat_human_age = 0
    elif 15 <= cat_age <= 23:
        cat_human_age = 1
    else:
        cat_human_age = 2 + (cat_age -24) // 4

    if dog_age <= 14:
        dog_human_age = 0
    elif 15 <= dog_age <= 23:
        dog_human_age = 1
    else:
        dog_human_age = 2 + (dog_age -24) // 5
    return [cat_human_age, dog_human_age]

