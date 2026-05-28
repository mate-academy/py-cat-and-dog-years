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
    human_age = [0, 0]

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Cat age and dog age must be integer type!!!")

    if (cat_age < 0 or cat_age > 100) or (dog_age < 0 or dog_age > 100):
        return human_age

    for age in range(1, cat_age + 1):
        if age == 15:
            human_age[0] += 1
        if age == 24:
            human_age[0] += 1
        if age > 24 and (age - 24) % 4 == 0:
            human_age[0] += 1

    for age in range(1, dog_age + 1):
        if age == 15:
            human_age[1] += 1
        if age == 24:
            human_age[1] += 1
        if age > 24 and (age - 24) % 5 == 0:
            human_age[1] += 1

    return human_age
