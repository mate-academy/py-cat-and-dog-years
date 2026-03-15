def get_human_age(cat_age: int, dog_age: int) -> list:

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Both cat_age and dog_age must be integers.")

    if isinstance(cat_age, bool) or isinstance(dog_age, bool):
        raise TypeError("Both cat_age and dog_age must be integers, not boolean.")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Both cat_age and dog_age must be non-negative integers.")

    # Calculate human age for cat
    if cat_age < 15:
        cat_human_age = 0
    elif cat_age < 24:
        cat_human_age = 1
    else:
        cat_human_age = 2 + (cat_age - 24) // 4

    # Calculate human age for dog
    if dog_age < 15:
        dog_human_age = 0
    elif dog_age < 24:
        dog_human_age = 1
    else:
        dog_human_age = 2 + (dog_age - 24) // 5

    return [cat_human_age, dog_human_age]
