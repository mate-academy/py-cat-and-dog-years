def get_human_age(cat_age: int, dog_age: int) -> list:
    step_dog = 5
    step_cat = 4
    result_list = []

    if cat_age < 15:
        human_cat_age = 0
    elif cat_age < 24:
        human_cat_age = 1
    else:
        human_cat_age = 2 + (cat_age - 24) // step_cat

    result_list.append(human_cat_age)

    if dog_age < 15:
        human_dog_age = 0
    elif dog_age < 24:
        human_dog_age = 1
    else:
        human_dog_age = 2 + (dog_age - 24) // step_dog

    result_list.append(human_dog_age)

    return result_list
