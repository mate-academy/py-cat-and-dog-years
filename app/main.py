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
    result = [0, 0]

    for i in range(cat_age):
        if i == 0 and cat_age >= 15:
            result[0] += 1
            cat_age -= 15
        elif i == 1 and cat_age >= 9:
            result[0] += 1
            cat_age -= 9
        elif i > 1:
            result[0] += cat_age // 4
            break
        else:
            break

    for i in range(dog_age):
        if i == 0 and dog_age >= 15:
            result[1] += 1
            dog_age -= 15
        elif i == 1 and dog_age >= 9:
            result[1] += 1
            dog_age -= 9
        elif i > 1:
            result[1] += dog_age // 5
            break
        else:
            break

    return result
