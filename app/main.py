def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Values should be integers")
    if cat_age < 0 or dog_age < 0:
        return []
    human_age = []
    animal_ages = [cat_age, dog_age]
    counter = 0
    for age in animal_ages:
        if age >= 24:
            if counter == 0:
                human_age.append((age - 24) // 4 + 2)
            else:
                human_age.append((age - 24) // 5 + 2)
            counter += 1
        elif age >= 15:
            human_age.append(1)
        else:
            human_age.append(0)
    return human_age
