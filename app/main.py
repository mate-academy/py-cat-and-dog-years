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
    # Write your tests first, then implement the logic
    def cat_to_human_age(age: int) -> int:
        if age <= 14:
            return 0
        if 15 <= age <= 23:
            return 1
        if 24 == age:
            return 2
        return 2 + (age - 24) // 4

    def dog_to_human_age(age: int) -> int:
        if age <= 14:
            return 0
        if 15 <= age <= 23:
            return 1
        if 24 == age:
            return 2
        return 2 + (age - 24) // 5
    return [cat_to_human_age(cat_age), dog_to_human_age(dog_age)]
