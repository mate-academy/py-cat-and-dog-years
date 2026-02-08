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
        raise TypeError("cat_age and dog_age must be integers")

    if cat_age < 0 or dog_age < 0 or cat_age > 100 or dog_age > 100:
        raise ValueError("Age is out of realistic range")

    cat_human_age = convert_to_human_age(cat_age, 15, 9, 4)
    dog_human_age = convert_to_human_age(dog_age, 15, 9, 5)
    return [int(cat_human_age), int(dog_human_age)]


def convert_to_human_age(
    animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    animal_age = int(animal_age)
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year
