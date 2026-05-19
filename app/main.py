def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise ValueError("Arguments must be integer")
    if not cat_age >= 0 or not dog_age >= 0:
        raise ValueError("Arguments must be Not negative")
    if not cat_age <= 100 or not dog_age <= 100:
        raise ValueError("Arguments must be Not very big")
    if 0 <= cat_age <= 14:
        cat_human_age = 0
    if 0 <= dog_age <= 14:
        dog_human_age = 0
    if 15 <= cat_age < 24:
        cat_human_age = 1
    if 15 <= dog_age < 24:
        dog_human_age = 1
    if 24 <= cat_age:
        cat_human_age = int(2 + (cat_age - 24) / 4)
    if 24 <= dog_age:
        dog_human_age = int(2 + (cat_age - 24) / 5)
    return [cat_human_age, dog_human_age]
