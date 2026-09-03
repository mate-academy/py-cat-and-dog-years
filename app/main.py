def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_age = 0 if cat_age < 15 else 1 \
        if cat_age < 24 else 2 + (cat_age - 24) // 4
    dog_human_age = 0 if dog_age < 15 else 1 \
        if dog_age < 24 else 2 + (dog_age - 24) // 5

    return [cat_human_age, dog_human_age]
