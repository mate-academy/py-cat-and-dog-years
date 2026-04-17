def get_human_age(cat_age: int, dog_age: int) -> list:
    # Calculate Cat Age
    if cat_age < 15:
        cat_h = 0
    elif cat_age < 24:
        cat_h = 1
    else:
        # 2 years for the first 24, plus 1 for every 4 years after
        cat_h = 2 + (cat_age - 24) // 4

    # Calculate Dog Age
    if dog_age < 15:
        dog_h = 0
    elif dog_age < 24:
        dog_h = 1
    else:
        # 2 years for the first 24, plus 1 for every 5 years after
        dog_h = 2 + (dog_age - 24) // 5

    return [cat_h, dog_h]
