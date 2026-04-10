def get_human_age(cat_age: int, dog_age: int) -> list:

    if 1 <= cat_age <= 14:
        cat_human_age = 0
    elif 15 <= cat_age <= 23:
        cat_human_age = 1
    else:
        step = 0
        cat_human_age = 2
        for i in range(24, cat_age):
            step += 1
            if step % 4 == 0:
                cat_human_age += 1

    if 1 <= dog_age <= 14:
        dog_human_age = 0
    elif 15 <= cat_age <= 23:
        dog_human_age = 1
    else:
        step = 0
        dog_human_age = 2
        for i in range(24, dog_age):
            step += 1
            if step % 5 == 0:
                dog_human_age += 1


    if cat_age == 0:
        cat_human_age = 0

    if dog_age == 0:
        dog_human_age = 0

    return [cat_human_age, dog_human_age]

print(get_human_age(28, 24))

def year_converter(animal_year: int, coefficient: int) -> int:
    if animal_year == 0:
        return 0

    if 1 <= animal_year <= 14:
        human_age = 0
    elif 15 <= animal_year <= 23:
        human_age = 1
    else:
        step = 0
        human_age = 2
        for i in range(24, animal_year):
            step += 1
            if step % coefficient == 0:
                human_age += 1

    return human_age