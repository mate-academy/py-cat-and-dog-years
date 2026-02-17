def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("cat_age and dog_age cannot be negative")
    human_age = [
        (cat_age >= 15)
        + (cat_age >= 24)
        + max(0, (cat_age - 24) // 4),
        (dog_age >= 15)
        + (dog_age >= 24)
        + max(0, (dog_age - 24) // 5)
    ]
    return human_age
