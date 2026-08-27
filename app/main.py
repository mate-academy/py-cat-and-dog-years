def convert_to_human(pet_age: int, step: int) -> int:
    pet_human_age = 0

    if pet_age >= 15:
        pet_human_age += 1

    if pet_age >= 24:
        pet_human_age += 1

    if pet_age >= 28:
        pet_age -= 24
        pet_human_age += pet_age // step

    return pet_human_age


def get_human_age(cat_age: int, dog_age: int) -> list:

    if not isinstance(cat_age, int):
        raise TypeError("cat_age must be an integer")
    if not isinstance(dog_age, int):
        raise TypeError("dog_age must be an integer")

    dog_human_age = convert_to_human(dog_age, 5)
    cat_human_age = convert_to_human(cat_age, 4)

    return [cat_human_age, dog_human_age]
