def calculate_single_human_age(age: int, step_after_24: int) -> int:
    human_age = 0

    if age < 15:
        return 0
    human_age += 1
    age -= 15

    if age < 9:
        return human_age
    human_age += 1
    age -= 9
    human_age += age // step_after_24

    return human_age


def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human = calculate_single_human_age(cat_age, 4)
    dog_human = calculate_single_human_age(dog_age, 5)

    return [cat_human, dog_human]
