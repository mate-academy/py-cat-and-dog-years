def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")

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
