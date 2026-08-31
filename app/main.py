def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    cat_human = 0
    dog_human = 0

    # Розрахунок для кота
    if cat_age >= 15:
        cat_human += 1
        if cat_age >= 24:
            cat_human += 1
            cat_human += (cat_age - 24) // 4

    # Розрахунок для собаки
    if dog_age >= 15:
        dog_human += 1
        if dog_age >= 24:
            dog_human += 1
            dog_human += (dog_age - 24) // 5

    return [cat_human, dog_human]
