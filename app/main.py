def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise ValueError("Parameters should be int!")
    converted_age = {"for_cat": 0, "for_dog": 0}
    if cat_age < 0:
        converted_age["for_cat"] = None
    if dog_age < 0:
        converted_age["for_dog"] = None
    if cat_age > 0:
        if cat_age // 15 >= 1:
            converted_age["for_cat"] += 1
            cat_age -= 15
            if cat_age // 9 >= 1:
                cat_age -= 9
                converted_age["for_cat"] += 1
                if cat_age // 4 >= 1:
                    while cat_age // 4 >= 1:
                        converted_age["for_cat"] += 1
                        cat_age -= 4
    if dog_age > 0:
        if dog_age // 15 >= 1:
            converted_age["for_dog"] += 1
            dog_age -= 15
            if dog_age // 9 >= 1:
                dog_age -= 9
                converted_age["for_dog"] += 1
                if dog_age // 5 >= 1:
                    while dog_age // 5 >= 1:
                        converted_age["for_dog"] += 1
                        dog_age -= 5
    return [converted_age["for_cat"], converted_age["for_dog"]]
