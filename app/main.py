def get_human_age(cat_age: int, dog_age: int) -> list:

    if cat_age < 0 and dog_age < 0:
        raise ValueError("Cat and dog ages cannot be negative.")

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("The 'cat_age' and 'dog_age' must be an integer.")

    if cat_age < 15:
        cat_result = 0
    elif cat_age == 15 or cat_age <= 23:
        cat_result = 1
    elif cat_age >= 24:
        cat_result = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        dog_result = 0
    elif dog_age == 15 or dog_age <= 23:
        dog_result = 1
    elif dog_age >= 24:
        dog_result = 2 + (dog_age - 24) // 5

    return [cat_result, dog_result]
