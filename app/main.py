def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Pet's age should be >= 0")

    cat_human_age = count_human_age(cat_age, "cat")
    dog_human_age = count_human_age(dog_age, "dog")

    return [cat_human_age, dog_human_age]


def count_human_age(age: int, pet: str) -> int:
    pet_human_age = 0

    if age // 15 > 0:
        pet_human_age += 1
        if age > 23:
            if pet == "cat":
                pet_human_age += ((age - 24) // 4) + 1
            elif pet == "dog":
                pet_human_age += ((age - 24) // 5) + 1
    return pet_human_age
