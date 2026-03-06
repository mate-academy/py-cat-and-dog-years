def convert_pet_age(
    pet_age: int,
    theirt_age: int
) -> int:
    """
    Convert pet age to human years based on the given rules.

    Args:
        pet_age: Age of the pet in their years
        theirt_age: The age threshold for conversion

    Returns:
        The equivalent human age for the pet

    Examples:
        convert_pet_age(0, 15) == 0
        convert_pet_age(15, 15) == 1
        convert_pet_age(24, 24) == 2
    """
    if not isinstance(pet_age, int):
        raise TypeError("Pet age must be an integer.")

    if pet_age < 0:
        raise ValueError("Pet age must be a non-negative integer.")

    if pet_age < 15:
        return 0
    elif pet_age < 24:
        return 1
    else:
        return 1 + 1 + (pet_age - 24) // theirt_age


def get_human_age(
    cat_age: int,
    dog_age: int
) -> list:
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

    return [
        convert_pet_age(cat_age, 4),
        convert_pet_age(dog_age, 5)
    ]
