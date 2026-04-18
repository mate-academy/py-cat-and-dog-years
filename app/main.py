def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0:
        raise Exception("Cat age cannot be less than 0")
    elif cat_age > 100:
        raise Exception("Cat age must be less than 100")
    if cat_age < 15:
        cat_human = 0
    elif cat_age < 24:
        cat_human = 1
    else:
        cat_human = 2 + (cat_age - 24) // 4

    if dog_age < 0:
        raise Exception("Dog age cannot be less than 0")
    elif dog_age > 100:
        raise Exception("Dog age must be less than 100")
    if dog_age < 15:
        dog_human = 0
    elif dog_age < 24:
        dog_human = 1
    else:
        dog_human = 2 + (dog_age - 24) // 5

    result = [cat_human, dog_human]
    return result
