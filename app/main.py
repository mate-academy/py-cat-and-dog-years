def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Both cat_age and dog_age must be integers")
    cat_human_age = 0
    if cat_age >= 24:
        cat_human_age = 2 + (cat_age - 24) // 4
    elif cat_age >= 15:
        cat_human_age = 1

    dog_human_age = 0
    if dog_age >= 24:
        dog_human_age = 2 + (dog_age - 24) // 5
    elif dog_age >= 15:
        dog_human_age = 1

    return [cat_human_age, dog_human_age]
