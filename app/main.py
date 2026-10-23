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
    
    cat_result = 0
    dog_result = 0

    if cat_age >= 15:
        cat_result += 1
        cat_age -= 15

    if dog_age >= 15:
        dog_result += 1
        dog_age -= 15

    if cat_result == 1 and cat_age >= 9:
        cat_result += 1
        cat_age -= 9
    
    if dog_result == 1 and dog_age >= 9:
        dog_result += 1
        dog_age -= 9

    if cat_result == 2:
        cat_result += (cat_age // 4)

    if dog_result == 2:
        dog_result += (dog_age // 5)

    return [cat_result, dog_result]
