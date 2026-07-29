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

    # Define a single helper function for the shared logic
    def calculate_animal_age(age: int, divisor: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1

        return 2 + ((age - 24) // divisor)

    human_cat_age = calculate_animal_age(cat_age, divisor=4)
    human_dog_age = calculate_animal_age(dog_age, divisor=5)

    return [human_cat_age, human_dog_age]
