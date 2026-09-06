def get_human_age(cat_age: int, dog_age: int) -> list:

    if cat_age < 15:
        cat_human_age = 0
    elif cat_age < 24:
        cat_human_age = 1
    else:
        cat_human_age = 2
        cat_years = cat_age - 24

        while cat_years >= 4:
            cat_human_age += 1
            cat_years -= 4
    if dog_age < 15:
        dog_human_age = 0
    elif dog_age < 24:
        dog_human_age = 1
    else:
        dog_human_age = 2
        dog_years = dog_age - 24
        while dog_years >= 5:
            dog_human_age += 1
            dog_years -= 5
    return [cat_human_age, dog_human_age]
