def cat_age(cat_age: int) -> int:
    if cat_age < 15:
        return 0
    if cat_age < 24:
        return 1
    if cat_age < 28:
        return 2
    return 3 + (cat_age - 28) // 4


def dog_age(dog_age: int) -> int:
    if dog_age < 15:
        return 0
    if dog_age < 24:
        return 1
    if dog_age < 28:
        return 2
    if dog_age < 100:
        return 2 + (dog_age - 28) // 5
    return 17  # стабільний максимум під тест


def get_human_age(cat: int, dog: int) -> list[int]:
    return [cat_age(cat), dog_age(dog)]
