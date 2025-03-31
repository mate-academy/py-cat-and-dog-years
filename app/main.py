def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """
    Convert cat and dog ages to human-equivalent years.

    Args:
        cat_age (int): Age of the cat in cat years.
        dog_age (int): Age of the dog in dog years.

    Returns:
        list[int]: [human years for cat, human years for dog].
    """
    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(
    animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    """
    Helper function to convert an animal's age to human-equivalent years.

    Args:
        animal_age (int): Age of the animal in animal years.
        first_year (int): Equivalent human years for the first threshold.
        second_year (int): Equivalent human years for the second threshold.
        each_year (int): Equivalent human years for every additional year.

    Returns:
        int: Age in human-equivalent years.
    """
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year
