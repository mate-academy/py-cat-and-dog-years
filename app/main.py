def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_and_dog_ages: list[int] = [0, 0]

    if 15 <= cat_age <= 23:
        cat_and_dog_ages[0] = 1
    elif cat_age > 23:
        cat_and_dog_ages[0] = 1
        for age_of_cat in range(24, cat_age + 1, 4):
            cat_and_dog_ages[0] += 1

    if 15 <= dog_age <= 23:
        cat_and_dog_ages[1] = 1
    elif dog_age > 23:
        cat_and_dog_ages[1] = 1
        for age_of_dog in range(24, dog_age + 1, 5):
            cat_and_dog_ages[1] += 1

    return cat_and_dog_ages
