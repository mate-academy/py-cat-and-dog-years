def get_human_age(cat_age: int, dog_age: int) -> list:
    if isinstance(cat_age, int) and isinstance(dog_age, int):
        if cat_age < 15:
            res_cat_age = 0

        if dog_age < 15:
            res_dog_age = 0

        if cat_age >= 15:
            cat_age -= 15
            res_cat_age = 1
            if cat_age >= 9:
                cat_age -= 9
                res_cat_age += 1
                for _ in range(cat_age // 4):
                    res_cat_age += 1

        if dog_age >= 15:
            dog_age -= 15
            res_dog_age = 1
            if dog_age >= 9:
                dog_age -= 9
                res_dog_age += 1
                for _ in range(dog_age // 5):
                    res_dog_age += 1
        return [res_cat_age, res_dog_age]
    raise (TypeError)
