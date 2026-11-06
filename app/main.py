def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.
    """

    def calculate_human_years(animal_age: int, step: int) -> int:
        if animal_age < 15:
            return 0
        if animal_age < 24:
            return 1

        return 2 + (animal_age - 24) // step

    return [calculate_human_years(cat_age, 4),
            calculate_human_years(dog_age, 5)]
