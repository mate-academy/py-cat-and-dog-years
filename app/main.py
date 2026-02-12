# flake8: noqa: W293
from app.errors import OutOfRangeError


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
        raise TypeError("Cat and dog ages must be integers")
    if cat_age < 0 or dog_age < 0:
        raise OutOfRangeError("Cat and dog ages can't be negative")
    if cat_age > 200 or dog_age > 200:
        raise OutOfRangeError("Very large numbers")
    dog_counter = [15, 9, 5]
    cat_counter = [15, 9, 4]
    return [
        animal_age_check_new(cat_age, cat_counter),
        animal_age_check_new(dog_age, dog_counter),
    ]


def animal_age_check_new(age: int, age_step: list) -> int:
    if age < age_step[0]:
        return 0
    if age < age_step[0] + age_step[1]:
        return 1
    age -= (age_step[0] + age_step[1])
    return 2 + (age // age_step[2])
