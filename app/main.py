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

    def get_base_years(animal_age: int, coefficient: int) -> int:
        if type(animal_age) is not int:
            raise TypeError
        animal_human_age = 0
        if 15 <= animal_age <= 100:
            animal_human_age += 1
            animal_age -= 15
            if animal_age >= 9:
                animal_human_age += 1
                animal_age -= 9
                if animal_age >= 4:
                    animal_human_age += animal_age // coefficient
        return animal_human_age

    cat_human_age = get_base_years(cat_age, 4)
    dog_human_age = get_base_years(dog_age, 5)

    return [cat_human_age, dog_human_age]
