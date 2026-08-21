def calculate_years(age: int, step: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // step


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    cat_human = calculate_years(cat_age, 4)
    dog_human = calculate_years(dog_age, 5)
    return [cat_human, dog_human]
