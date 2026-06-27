def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_count = 0
    remainder = 0
    dog_human_count = 0
    remaind = 0

    if cat_age >= 15:
        cat_human_count += 1
        remainder = cat_age - 15
        if remainder >= 9:
            cat_human_count += 1
            remainder -= 9
    if remainder >= 4:
        result = remainder // 4
        cat_human_count += result

    if dog_age >= 15:
        dog_human_count += 1
        remaind = dog_age - 15
        if remaind >= 9:
            dog_human_count += 1
            remaind -= 9
    if remaind >= 5:
        resul = remaind // 5
        dog_human_count += resul
    return [cat_human_count, dog_human_count]
