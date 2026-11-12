from __future__ import annotations


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    cat_human_age = 0
    dog_human_age = 0

    if cat_age >= 15:
        cat_human_age += 1
        cat_age -= 15

        if cat_age >= 9:
            cat_human_age += 1
            cat_age -= 9

        cat_human_age += cat_age // 4
    else:
        cat_human_age += cat_age // 15

    if dog_age >= 15:
        dog_human_age += 1
        dog_age -= 15

        if dog_age >= 9:
            dog_human_age += 1
            dog_age -= 9

        dog_human_age += dog_age // 5
    else:
        dog_human_age += dog_age // 15

    return [cat_human_age, dog_human_age]
