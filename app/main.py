def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    if isinstance(cat_age, bool) or isinstance(dog_age, bool):
        raise TypeError

    if cat_age < 0 or dog_age < 0:
        raise ValueError
    cat_value = calculate_age(cat_age, "cat")
    dog_value = calculate_age(dog_age, "dog")
    return [cat_value, dog_value]


def calculate_age(age: int, animal: str) -> int:
    if age < 15:
        return 0
    elif age < 24:
        return 1
    else:
        if animal == "cat":
            div = ((age - 24) // 4) + 2
        else:
            div = ((age - 24) // 5) + 2
    return div


print(get_human_age(14, 14))
