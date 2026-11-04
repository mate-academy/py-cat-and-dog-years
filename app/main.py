def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human = 0
    cat_left = cat_age
    if cat_left >= 15:
        cat_human += 1
        cat_left -= 15
        if cat_left >= 9:
            cat_human += 1
            cat_left -= 9
            cat_human += cat_left // 4

    dog_human = 0
    dog_left = dog_age
    if dog_left >= 15:
        dog_human += 1
        dog_left -= 15
        if dog_left >= 9:
            dog_human += 1
            dog_left -= 9
            dog_human += dog_left // 5

    return [cat_human, dog_human]
