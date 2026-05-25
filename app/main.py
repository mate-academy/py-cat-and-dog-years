def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age should be a positive value")

    if cat_age > 120 or dog_age > 120:
        raise ValueError("Age should be less than 120")

    if 0 < cat_age <= 15:
        converted_cats_age = 1
    elif 16 < cat_age <= 24:
        converted_cats_age = 2
    elif cat_age >= 25:
        rest = cat_age - 25
        converted_cats_age = round(2 + (rest / 4))
    else:
        converted_cats_age = 0

    if 0 < dog_age <= 15:
        converted_dogs_age = 1
    elif 16 < dog_age <= 24:
        converted_dogs_age = 2
    elif dog_age >= 25:
        rest = dog_age - 25
        converted_dogs_age = round(2 + (rest // 5))
    else:
        converted_dogs_age = 0

    return [converted_cats_age, converted_dogs_age]
