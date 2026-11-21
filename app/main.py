def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Cat age and dog age must be positive")

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Cat age and dog age must be integers")

    if isinstance(cat_age, bool) or isinstance(dog_age, bool):
        raise TypeError("Cat age and dog age must be booleans")

    if cat_age < 24 and cat_age > 14:
        human_cat_age = 1
    else:
        human_cat_age = 0
    if dog_age < 24 and dog_age > 14:
        human_dog_age = 1
    else:
        human_dog_age = 0

    if cat_age >= 24:
        human_cat_age = (cat_age - 24) // 4 + 2
    if dog_age >= 24:
        human_dog_age = (dog_age - 24) // 5 + 2

    return [human_cat_age, human_dog_age]
