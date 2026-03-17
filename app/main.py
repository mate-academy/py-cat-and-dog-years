def get_human_age(cat_age: int, dog_age: int) -> list:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Ages must be integers")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    cat_human = 0
    if cat_age >= 24:
        cat_human = 2 + (cat_age - 24) // 4
    elif cat_age >= 15:
        cat_human = 1

    dog_human = 0
    if dog_age >= 24:
        dog_human = 2 + (dog_age - 24) // 5
    elif dog_age >= 15:
        dog_human = 1

    return [cat_human, dog_human]
