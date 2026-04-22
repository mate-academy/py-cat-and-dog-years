def get_human_age(cat_age: int, dog_age: int) -> list:
    if isinstance(cat_age, bool) or isinstance(dog_age, bool):
        raise TypeError("cat_age and dog_age must be integers")
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")

    cat_human_age = 0
    if 15 <= cat_age < 24:
        cat_human_age = 1
    if cat_age >= 24:
        cat_human_age = 2 + ((cat_age - 24) // 4)

    dog_human_age = 0
    if 15 <= dog_age < 24:
        dog_human_age = 1
    if dog_age >= 24:
        dog_human_age = 2 + ((dog_age - 24) // 5)

    return [cat_human_age, dog_human_age]
