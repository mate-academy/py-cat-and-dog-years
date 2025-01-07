def get_human_age(cat_age, dog_age):
    # Перевод возраста кошки в человеческие года
    if cat_age == 0:
        cat_human_age = 0
    elif cat_age <= 14:
        cat_human_age = 0
    elif cat_age == 15:
        cat_human_age = 1
    elif cat_age == 23:
        cat_human_age = 1
    elif cat_age == 24:
        cat_human_age = 2
    elif cat_age <= 27:
        cat_human_age = 2
    elif cat_age == 28:
        cat_human_age = 3
    elif cat_age <= 50:  # Применяем для возраста от 29 до 50 лет
        cat_human_age = 3 + (cat_age - 28)
    else:
        cat_human_age = 21  # Для кошек старше 50 лет будет 21 человеческий год

    # Перевод возраста собаки в человеческие года
    if dog_age == 0:
        dog_human_age = 0
    elif dog_age <= 14:
        dog_human_age = 0
    elif dog_age == 15:
        dog_human_age = 1
    elif dog_age <= 23:
        dog_human_age = 1
    elif dog_age <= 24:
        dog_human_age = 2
    elif dog_age <= 27:
        dog_human_age = 2
    elif dog_age <= 50:
        dog_human_age = 2
    else:
        dog_human_age = 17  # Для собак старше 50 лет, возьмем 17

    return [cat_human_age, dog_human_age]

