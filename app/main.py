def get_human_age(cat_age: int, dog_age: int) -> list:

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    if cat_age < 0 or cat_age > 120 or dog_age < 0 or dog_age > 120:
        raise ValueError

    dog_human_years = 0

    if dog_age >= 15:
        dog_human_years += 1
        dog_age -= 15

        if dog_age >= 9:
            dog_human_years += 1
            dog_age -= 9

            dog_human_years += dog_age // 5

    cat_human_years = 0

    if cat_age >= 15:
        cat_human_years += 1
        cat_age -= 15

        if cat_age >= 9:
            cat_human_years += 1
            cat_age -= 9

            cat_human_years += cat_age // 4

    return [cat_human_years, dog_human_years]
