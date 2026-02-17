def get_human_age(cat_age: int, dog_age: int) -> list:

    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Invalid input")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Input must be positive integer")

    human_years = [0, 0]

    animal_years = [cat_age, dog_age]

    for index, years in enumerate(animal_years):
        human_year = 0
        if years >= 15:
            human_year += 1
            years -= 15

            if years >= 9:
                human_year += 1
                years -= 9

                if years >= 0:
                    if index == 0:
                        human_year += years // 4
                    elif index == 1:
                        human_year += years // 5
        else:
            years = 0

        human_years[index] = human_year

    return human_years
