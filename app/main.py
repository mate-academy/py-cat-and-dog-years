def get_human_age(cat_age: int, dog_age: int) -> list:
    if isinstance(cat_age, int) is False or isinstance(dog_age, int) is False:
        raise TypeError

    if cat_age > 1000 or dog_age > 1000:
        raise ValueError
    if cat_age < 0 or dog_age < 0:
        raise ValueError
    cat_years = cat_age
    dog_years = dog_age
    cat_human = 0
    dog_human = 0
    while True:

        if cat_years < 15:
            break
        cat_years -= 15
        cat_human += 1
        if cat_years - 9 >= 0:
            cat_years -= 9
            cat_human += 1
        else:
            break
        if cat_years - 4 >= 0:
            while True:
                cat_years -= 4
                cat_human += 1
                if (cat_years - 4) < 0:
                    break
        break

    while True:

        if dog_years < 15:
            break
        dog_years -= 15
        dog_human += 1
        if dog_years - 9 >= 0:
            dog_years -= 9
            dog_human += 1
        else:
            break
        if dog_years - 5 >= 0:
            while True:
                dog_years -= 5
                dog_human += 1
                if (dog_years - 5) < 0:
                    break
    return [cat_human, dog_human]
