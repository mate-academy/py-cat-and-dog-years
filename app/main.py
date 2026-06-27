def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_count = 0
    dog_human_count = 0

    if cat_age >= 15:
        cat_human_count += 1
        remainder = cat_age - 15

        if remainder >= 9:
            cat_human_count += 1
            remainder -= 9
            cat_human_count += remainder // 4

    if dog_age >= 15:
        dog_human_count += 1
        remainder = dog_age - 15

        if remainder >= 9:
            dog_human_count += 1
            remainder -= 9
            dog_human_count += remainder // 5

    return [cat_human_count, dog_human_count]
