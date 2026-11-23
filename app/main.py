def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_age = 0
    dog_human_age = 0

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Invalid type! The pet's age should be integer!")

    elif cat_age < 0 or dog_age < 0:
        raise ValueError("The pet's age should be greater than 0 !")

    if cat_age in range(15, 24):
        cat_human_age = 1
    elif cat_age >= 24:
        cat_human_age = 2 + (cat_age - 24) // 4

    if dog_age in range(15, 24):
        dog_human_age = 1
    elif dog_age >= 24:
        dog_human_age = 2 + (dog_age - 24) // 5

    return [cat_human_age, dog_human_age]
