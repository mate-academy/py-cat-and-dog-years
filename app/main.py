def get_human_age(cat_age: int, dog_age: int) -> list:
    if isinstance(cat_age, bool) or isinstance(dog_age, bool):
        raise TypeError("This type can't be the age")
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("This type can't be the age")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age can't be negative")

    cat_result = 0
    dog_result = 0

    if cat_age >= 15:
        cat_result += 1
        cat_age -= 15
        if cat_age >= 9:
            cat_result += 1
            cat_age -= 9
            cat_result += cat_age // 4

    if dog_age >= 15:
        dog_result += 1
        dog_age -= 15
        if dog_age >= 9:
            dog_result += 1
            dog_age -= 9
            dog_result += dog_age // 5

    return [cat_result, dog_result]
