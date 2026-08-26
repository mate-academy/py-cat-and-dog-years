from app.exception import InvalidParameter, InvalidParameterType


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
        raise InvalidParameterType("Age must be an integer!")
    if cat_age < 0 or dog_age < 0:
        raise InvalidParameter("Age must be a positive number!")
    cat_to_human = 0
    dogs_to_human = 0

    if cat_age >= 15:
        cat_to_human += 1
        cat_age -= 15
        if cat_age >= 9:
            cat_to_human += 1
            cat_age -= 9
            while cat_age >= 4:
                cat_to_human += 1
                cat_age -= 4

    if dog_age >= 15:
        dogs_to_human += 1
        dog_age -= 15
        if dog_age >= 9:
            dogs_to_human += 1
            dog_age -= 9
            while dog_age >= 5:
                dogs_to_human += 1
                dog_age -= 5

    return [cat_to_human, dogs_to_human]
