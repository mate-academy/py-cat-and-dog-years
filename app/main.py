def get_human_age(cat_age: int, dog_age: int) -> list:

    if cat_age < 15 and dog_age < 15:
        return [0, 0]
    elif 15 <= cat_age < 24 and 15 <= dog_age < 24:
        return [1, 1]
    elif cat_age >= 24 and dog_age >= 24:
        return [2 + (cat_age - 24) // 4, 2 + (dog_age - 24) // 5]
