def get_human_age(cat_age: int, dog_age: int) -> list:
    human_ages = []
    if cat_age < 15:
        human_ages.append(0)
    elif 15 <= cat_age < 24:
        human_ages.append(1)
    elif cat_age >= 24:
        human_ages.append((cat_age - 24) // 4 + 2)
    if dog_age < 15:
        human_ages.append(0)
    elif 15 <= dog_age < 24:
        human_ages.append(1)
    elif dog_age >= 24:
        human_ages.append((dog_age - 24) // 5 + 2)
    return human_ages
