def get_human_age(cat_age: int, dog_age: int) -> list:
    if (isinstance(cat_age, int)
            and isinstance(dog_age, int)
            and cat_age >= 0 and dog_age >= 0):
        if cat_age < 24:
            cat_result = cat_age // 15
        else:
            cat_result = 2 + (cat_age - 24) // 4
        if dog_age < 24:
            dog_result = dog_age // 15
        else:
            dog_result = 2 + (dog_age - 24) // 5
    return [cat_result, dog_result]
