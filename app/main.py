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
        raise TypeError
    
    result = [0, 0]
    cat_age_checker = True
    dog_age_checker = True

    if cat_age < 15:
        cat_age_checker = False

    if dog_age < 15:
        dog_age_checker = False

    if cat_age >= 15 and cat_age_checker:
        cat_age -= 15
        result[0] += 1

    if dog_age >= 15 and dog_age_checker:
        dog_age -= 15
        result[1] += 1

    if cat_age < 9:
        cat_age_checker = False

    if dog_age < 9:
        dog_age_checker = False

    if cat_age >= 9 and cat_age_checker:
        cat_age -= 9
        result[0] += 1

    if dog_age >= 9 and dog_age_checker:
        dog_age -= 9
        result[1] += 1

    while cat_age_checker:
        if cat_age >= 4:
            cat_age -= 4
            result[0] += 1
        if cat_age < 4:
            break

    while dog_age_checker:
        if dog_age >= 5:
            dog_age -= 5
            result[1] += 1
        if dog_age < 5:
            break

    return result
