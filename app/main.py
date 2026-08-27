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
        raise TypeError("Cat and dog age must be integer")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Cat and dog age cannot be negative number")
    if cat_age > 100 or dog_age > 100:
        raise ValueError("Unrealisticly big age value")
    human_age = []
    human_cat_age = min(cat_age , 15) // 15
    if max(cat_age - 15, 0):
        human_cat_age += min(max(cat_age - 15, 0), 9) // 9
    if max(cat_age - 15 - 9, 0):
        human_cat_age += max(cat_age - 24, 0) // 4
    human_age.append(human_cat_age)
    human_dog_age = min(dog_age, 15) // 15
    if max(dog_age - 15, 0):
        human_dog_age += min(max(dog_age - 15, 0), 9) // 9
    if max(dog_age - 15 - 9, 0):
        human_dog_age += max(dog_age - 24, 0) // 5
    human_age.append(human_dog_age)
    return human_age
