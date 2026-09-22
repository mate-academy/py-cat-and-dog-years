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
    if cat_age < 0 or dog_age < 0:
        raise ValueError("All arguments should be positive numbers")
    cat_human_age = get_human_age_helper(cat_age, 4)
    dog_human_age = get_human_age_helper(dog_age, 5)
    return [cat_human_age, dog_human_age]


def get_human_age_helper(animal_age: int,
                         number_of_years_per_additional_human_year: int
                         ) -> int:
    animal_human_age = 0
    if 24 > animal_age >= 15:
        animal_human_age = 1
    if animal_age == 24:
        animal_human_age = 2
    if animal_age > 24:
        animal_human_age = (2 + (animal_age - 24)
                            // number_of_years_per_additional_human_year)
    return animal_human_age
