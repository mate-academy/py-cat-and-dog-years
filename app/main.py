def get_human_age(cat_age: int, dog_age: int) -> list:
    rules_cat  = [15, 9 , 4]
    rules_dog  = [15, 9 , 5]

    cat_human_age = 0
    cat = cat_age

    for r in rules_cat[:2]:
        if cat >= r:
            cat -= r
            cat_human_age += 1
        else:
            break

    if cat_human_age == 2:
        cat_human_age += cat // rules_cat[2]

    dog_human_age = 0
    dog = dog_age

    for r in rules_dog[:2]:
        if dog >= r:
            dog -= r
            dog_human_age += 1
        else:
            break

    if dog_human_age == 2:
        dog_human_age += dog // rules_dog[2]

    return [cat_human_age, dog_human_age]
