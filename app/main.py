def get_human_age(cat_age: int, dog_age: int) -> list:

    count_cats_ages = 0
    count_dog_ages = 0
    in_human_age = []

    if cat_age < 15:
        in_human_age.append(count_cats_ages)
    elif cat_age < 24:
        count_cats_ages += 1
        in_human_age.append(count_cats_ages)
    else :
        count_cats_ages += 2
        cat_age -= 24
        count_cats_ages += cat_age // 4
        in_human_age.append(count_cats_ages)

    if dog_age < 15:
        in_human_age.append(count_dog_ages)
    elif dog_age < 24:
        count_dog_ages += 1
        in_human_age.append(count_dog_ages)
    else:
        count_dog_ages += 2
        dog_age -= 24
        count_dog_ages += dog_age // 5
        in_human_age.append(count_dog_ages)

    return in_human_age
