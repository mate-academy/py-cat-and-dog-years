from math import floor


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
    human_dog_age = 0
    human_cat_age = 0
    if cat_age >= 0 and dog_age >= 0:
        if dog_age < 15:
            human_dog_age = 0
        elif 15 <= dog_age < 24:
            human_dog_age = 1
        elif dog_age >= 24:
            human_dog_age=_age = 2 + floor((dog_age - 24)/5)
        if cat_age < 15:
            human_cat_age = 0
        elif 15 <= cat_age < 24:
            human_cat_age = 1
        elif cat_age >= 24:
            human_cat_age = 2 + floor((cat_age - 24)/4)

    return [human_cat_age, human_dog_age]

get_human_age(24, 24)
