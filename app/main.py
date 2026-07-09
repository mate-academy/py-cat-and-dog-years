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
    def count_age(age_raw: int, step: int) -> int:
        age = int(age_raw)
        if age <= 14:
            return 0
        elif age in range(15, 25):
            return 1
        elif age in range(25, 30):
            return 2
        else:
            return (age - 30) // step + 2

    return [count_age(cat_age, 4), count_age(dog_age, 5)]
