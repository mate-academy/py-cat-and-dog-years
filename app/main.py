def get_human_age(cat_age: int, dog_age: int) -> list:

    if not isinstance(cat_age, int):
        raise TypeError("Cat age must be an integer.")
    if not isinstance(dog_age, int):
        raise TypeError("Dog age must be an integer.")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")

    human_cat = 0
    human_dog = 0

# Cat
    cat_count = 0

    if cat_age >= 15:
        human_cat = 1

        if cat_age >= 24:
            human_cat = 2

            cat_leftover = cat_age - 24

            while cat_leftover >= 4:
                cat_leftover -= 4
                cat_count += 1

    human_cat += cat_count

# Dog
    dog_count = 0

    if dog_age >= 15:
        human_dog = 1

        if dog_age >= 24:
            human_dog = 2

            dog_leftover = dog_age - 24

            while dog_leftover >= 5:
                dog_leftover -= 5
                dog_count += 1

    human_dog += dog_count

    return [human_cat, human_dog]
