def calculate_human_age(age: int, step: int) -> int:
    if age == 0:
        return 0
    elif age < 15:
        return 0
    elif age < 24:
        return 1
    elif age == 24:
        return 2
    else:
        return 2 + (age - 24) // step


def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be an integer!")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age must be positive!")
    cat_human_age = calculate_human_age(cat_age, step=4)
    dog_human_age = calculate_human_age(dog_age, step=5)
    return [cat_human_age, dog_human_age]
