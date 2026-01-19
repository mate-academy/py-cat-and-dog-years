def get_human_age(cat_age: int, dog_age: int) -> list:
    human_age = [0, 0]
    if cat_age >= 15:
        human_age[0] += 1
    remaining1 = cat_age - 15
    if remaining1 >= 9:
        human_age[0] += 1
        remaining1 -= 9
        extra_years_cats = remaining1 // 4
        human_age[0] += extra_years_cats
    if dog_age >= 15:
        human_age[1] += 1
    remaining2 = dog_age - 15
    if remaining2 >= 9:
        human_age[1] += 1
        remaining2 -= 9
        extra_years_dogs = remaining2 // 5
        human_age[1] += extra_years_dogs
    return human_age
