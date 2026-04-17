def get_human_age(cat_age: int, dog_age: int) -> list:
    if not (isinstance(cat_age, int) and isinstance(dog_age, int)):
        raise TypeError("Values must be integers.")
    if not (0 <= cat_age <= 100 and 0 <= dog_age <= 100):
        raise ValueError("Values must be non-negative integers "
                         "between 0 and 100.")
    cat_human = (cat_age >= 15) + (cat_age >= 24) + max(0, cat_age - 24) // 4
    dog_human = (dog_age >= 15) + (dog_age >= 24) + max(0, dog_age - 24) // 5

    return [cat_human, dog_human]
