def get_human_age(cat_age: int, dog_age: int) -> list:
    human_age = [0, 0]

    if cat_age < 15:
        human_age[0] = 0
    elif cat_age < 24:
        human_age[0] = 1
    else:
        aux_variable = cat_age - 23
        if aux_variable % 4 == 0:
            aux_variable -= 1
        human_age[0] = (aux_variable // 4) + 2

    if dog_age < 15:
        human_age[1] = 0
    elif dog_age < 24:
        human_age[1] = 1
    else:
        aux_variable = dog_age - 23
        if aux_variable % 5 == 0:
            aux_variable -= 1
        human_age[1] = (aux_variable // 5) + 2
    return human_age
