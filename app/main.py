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
    def convert(age: int, first: int, second: int, step: int) -> int:
        if age < first:
            return 0
        if age < first + second:
            return 1
        age -= first + second
        return 2 + age // step

    cat_human = convert(cat_age, 15, 9, 4)
    dog_human = convert(dog_age, 15, 9, 5)

    return [cat_human, dog_human]
