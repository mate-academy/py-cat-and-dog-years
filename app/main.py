def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age can not be < 0")
    human_age = [0, 0]
    age_after_24 = (4, 5)
    i = -1
    for animal_age in (cat_age, dog_age):
        i += 1
        if not animal_age >= 15:
            continue
        human_age[i] += 1
        animal_age -= 15
        if not animal_age >= 9:
            continue
        human_age[i] += 1
        animal_age -= 9
        while animal_age >= age_after_24[i]:
            animal_age -= age_after_24[i]
            human_age[i] += 1

    return human_age
