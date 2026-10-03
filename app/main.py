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
    def convert_age(age: int, second_threshold: int, third_rate: int) -> int:
        if age < 15:
            return 0
        elif age < 15 + 9:  # First 15 years = 1, next 9 years = 1 more
            return 1
        else:
            # After 24 years: add 1 for every N years (4 for cats, 5 for dogs)
            remaining = age - 24
            return 2 + remaining // third_rate

    cat_human_age = convert_age(cat_age, 24, 4)
    dog_human_age = convert_age(dog_age, 24, 5)

    return [cat_human_age, dog_human_age]
