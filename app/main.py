def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Cat and Dog age must be integers")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Cat and Dog age must be positive")
    if cat_age <= 14:
        cat_age_result = 0
    elif cat_age <= 23:
        cat_age_result = 1
    else:
        cat_age_result = 2 + (cat_age - 24) // 4
    if dog_age <= 14:
        dog_age_result = 0
    elif dog_age <= 23:
        dog_age_result = 1
    else:
        dog_age_result = 2 + (dog_age - 24) // 5

    return [cat_age_result, dog_age_result]
