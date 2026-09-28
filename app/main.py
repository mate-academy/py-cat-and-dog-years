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
    """
    # TODO: Implement this function
    # Write your tests first, then implement the logic
    if (cat_age < 15):
        cat_human_age = 0
    elif (cat_age >= 15 and cat_age <= 23):
        cat_human_age = 1
    elif (cat_age > 23 and cat_age <= 27):
        cat_human_age = 2
    elif (cat_age > 27):
        cat_human_age = 2 + (cat_age - 24) // 4
    if (dog_age < 15):
        dog_human_age = 0
    elif (dog_age >= 15 and dog_age <= 23):
        dog_human_age = 1
    elif (dog_age > 23 and dog_age <= 27):
        dog_human_age = 2
    elif (dog_age > 27):
        dog_human_age = 2 + (dog_age - 24) // 5
    return [cat_human_age, dog_human_age]
