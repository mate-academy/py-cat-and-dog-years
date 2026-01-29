def get_human_age(cat_age: int, dog_age: int) -> list:
    if isinstance(cat_age, bool) or not isinstance(cat_age, int):
        raise TypeError

    if isinstance(dog_age, bool) or not isinstance(dog_age, int):
        raise TypeError

    if cat_age < 0:
        raise ValueError
    
    if dog_age < 0:
        raise ValueError

    if cat_age < 15:
        cat_human = 0
    elif cat_age < 24:
        cat_human = 1
    else:
        cat_human = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        dog_human = 0
    elif dog_age < 24:
        dog_human = 1
    else:
        dog_human = 2 + (dog_age - 24) // 5
    return [cat_human, dog_human]
