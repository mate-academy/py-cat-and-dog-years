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
    index = 0
    years = 4
    for age in [cat_age, dog_age]:
        counter = age
        if 14 < age:
            human_age[index] += 1
            counter -= 15
            if 23 < age:
                human_age[index] += 1
                counter -= 9
                while counter >= years:
                    human_age[index] += 1
                    counter -= years
        index += 1
        years += 1

    return human_age
