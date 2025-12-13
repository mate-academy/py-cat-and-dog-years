def get_human_age(cat_age: int, dog_age: int) -> list:
    # Cat age conversion
    cat_human = 0
    age = cat_age

    if age >= 15:
        cat_human = 1
        age -= 15

        if age >= 9:
            cat_human += 1
            age -= 9
            cat_human += age // 4

    # Dog age conversion
    dog_human = 0
    age = dog_age

    if age >= 15:
        dog_human = 1
        age -= 15

        if age >= 9:
            dog_human += 1
            age -= 9
            dog_human += age // 5

    return [cat_human, dog_human]
