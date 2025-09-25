def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    # 🔒 validações exigidas pelo checklist
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("cat_age and dog_age cannot be negative")

    # 🐱 cálculo para gatos
    if cat_age == 0:
        cat_human = 0
    elif cat_age < 15:
        cat_human = 0
    elif cat_age < 24:
        cat_human = 1
    elif cat_age < 28:
        cat_human = 2
    else:
        # depois de 28, cada 4 anos de gato = +1 humano
        cat_human = 2 + ((cat_age - 24) // 4)

    # 🐶 cálculo para cães
    if dog_age == 0:
        dog_human = 0
    elif dog_age < 15:
        dog_human = 0
    elif dog_age < 28:
        dog_human = 1
    elif dog_age < 29:
        dog_human = 2
    else:
        # depois de 29, cada 5 anos de cão = +1 humano
        dog_human = 2 + ((dog_age - 24) // 5)

    return [cat_human, dog_human]
