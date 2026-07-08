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

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be an integer.")

    if (cat_age < 0 or dog_age < 0) or (cat_age > 400 or dog_age > 400):
        raise ValueError("Age must be a positive number.")

    # --- inner converter
    def convert_animal_to_human(
            animal_age: int,
            boundary_cond:
            tuple[int, int, int]
    ) -> int:

        human_years = 0

        if animal_age < boundary_cond[0]:
            return human_years

        human_years += 1
        animal_age -= boundary_cond[0]

        if animal_age < boundary_cond[1]:
            return human_years

        human_years += 1
        animal_age -= boundary_cond[1]

        # for case 3
        bound_age = boundary_cond[2]
        if animal_age >= bound_age:
            add_years = animal_age // bound_age
            human_years += add_years

        return human_years
    # --- end of inner converter

    cat_to_human = convert_animal_to_human(cat_age, (15, 9, 4))
    dog_to_human = convert_animal_to_human(dog_age, (15, 9, 5))

    return [cat_to_human, dog_to_human]
