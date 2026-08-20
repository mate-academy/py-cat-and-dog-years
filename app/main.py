def get_human_age(cat_age: int, dog_age: int) -> list:
    if (type(cat_age) is not int
            or type(dog_age) is not int):
        raise ValueError("Incorrect types of arguments, should be type: int")
    human_years = [0, 0]
    if cat_age >= 15:
        ages = [15, 9, 4]
        iter_count = 0
        while cat_age > 0:
            age_cost = ages[min(iter_count, 2)]
            cat_age -= age_cost
            if cat_age < 0:
                break
            human_years[0] += 1
            iter_count += 1
    if dog_age >= 15:
        ages = [15, 9, 5]
        iter_count = 0
        while dog_age > 0:
            age_cost = ages[min(iter_count, 2)]
            dog_age -= age_cost
            if dog_age < 0:
                break
            human_years[1] += 1
            iter_count += 1
    return human_years
