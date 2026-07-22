def convert_to_human_age(animal_age: int, years_step: int) -> int:
    if animal_age <= 14:
        return 0
    elif 15 <= animal_age <= 23:
        return 1
    else:
        return 2 + (animal_age - 24) // years_step


def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_age = convert_to_human_age(cat_age, 4)
    dog_human_age = convert_to_human_age(dog_age, 5)
    return [cat_human_age, dog_human_age]
