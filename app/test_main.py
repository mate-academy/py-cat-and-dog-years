def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    # Перевірка типів
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")
    # Перевірка на негативні значення
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages must be non-negative")

    # Логіка для кота
    if cat_age <= 14:
        human_cat_age = 0
    elif 15 <= cat_age <= 23:
        human_cat_age = 1
    elif 24 <= cat_age <= 27:
        human_cat_age = 2
    elif 28 <= cat_age <= 29:
        human_cat_age = 3
    else:
        # Припустимо, кожен рік після 29 — це 1 людський рік
        human_cat_age = 3 + (cat_age - 29)

    # Логіка для собаки (відкоригована)
    if dog_age <= 14:
        human_dog_age = 0
    elif 15 <= dog_age <= 23:
        human_dog_age = 1
    elif 24 <= dog_age <= 27:
        human_dog_age = 2
    elif 28 <= dog_age <= 29:
        human_dog_age = 2  # Зверни увагу: тут 2, не 3
    else:
        # Кожен рік після 29 рахуємо як 1 людський рік
        human_dog_age = 2 + (dog_age - 29)

    return [human_cat_age, human_dog_age]
