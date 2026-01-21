def get_human_age(cat_age: int, dog_age: int) -> list:
    ls = [0, 0]
    human_c = 0
    if cat_age == 0:
        return [0, 0]
    if cat_age >= 15:
        human_c += 1
    if cat_age >= 24:
        human_c += 1
    extra = max(0, cat_age - 24)
    human_c += extra // 4
    human_d = 0
    if dog_age == 0:
        return [0, 0]
    if dog_age >= 15:
        human_d += 1
    if dog_age >= 24:
        human_d += 1
    extra = max(0, dog_age - 24)
    human_d += extra // 5
    ls[0] = human_c
    ls[1] = human_d
    return ls
