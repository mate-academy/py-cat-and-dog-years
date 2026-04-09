def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    # 2. Validación de Valores [Satisface test_should_handle_negative_numbers]
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    cat_human_age = 0
    dog_human_age = 0

    # Lógica de conversión para el Gato
    if cat_age >= 15:
        cat_human_age = 1
    if cat_age >= 24:
        cat_human_age = 2
    if cat_age > 24:
        cat_human_age += (cat_age - 24) // 4

    # Lógica de conversión para el Perro
    if dog_age >= 15:
        dog_human_age = 1
    if dog_age >= 24:
        dog_human_age = 2
    if dog_age > 24:
        dog_human_age += (dog_age - 24) // 5

    return [cat_human_age, dog_human_age]
