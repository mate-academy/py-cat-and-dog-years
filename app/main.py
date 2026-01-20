def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age can not be < 0")
    human_age = [0, 0]
    age_after_24 = (4, 5)
    i = -1
    for animal_age in (cat_age, dog_age):
        i += 1
        if animal_age >= 15:
            human_age[i] += 1
            animal_age -= 15
        else:
            continue
        if animal_age >= 9:
            human_age[i] += 1
            animal_age -= 9
        else:
            continue
        while animal_age >= age_after_24[i]:
            animal_age -= age_after_24[i]
            human_age[i] += 1

    return human_age
