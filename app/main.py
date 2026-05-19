def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_age = 0
    if cat_age >= 15:
        cat_age -= 15
        cat_human_age += 1
        if cat_age >= 9:
            cat_age -= 9
            cat_human_age += 1
            while cat_age >= 4:
                cat_age -= 4
                cat_human_age += 1

    dog_human_age = 0
    if dog_age >= 15:
        dog_age -= 15
        dog_human_age += 1
        if dog_age >= 9:
            dog_age -= 9
            dog_human_age += 1
            while dog_age >= 5:
                dog_age -= 5
                dog_human_age += 1

    return [cat_human_age, dog_human_age]


print(get_human_age(1, 0))
