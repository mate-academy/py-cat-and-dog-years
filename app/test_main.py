def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    # Перевірка типів
    if not isinstance(cat_age, int):
        raise TypeError("cat_age must be int")
    if not isinstance(dog_age, int):
        raise TypeError("dog_age must be int")
    
    # Перевірка на негативні значення
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages must be non-negative")

    # Логіка конвертації віку (приклад, можеш замінити на свою)
    def cat_to_human(age: int) -> int:
        if age <= 14:
            return 0
        elif age <= 23:
            return 1
        elif age <= 27:
            return 2
        elif age <= 100:
            return 3 + (age - 28) // 10  # приклад
    
    def dog_to_human(age: int) -> int:
        if age <= 14:
            return 0
        elif age <= 23:
            return 1
        elif age <= 29:
            return 2
        elif age <= 100:
            return 2 + (age - 30) // 5  # приклад

    return [cat_to_human(cat_age), dog_to_human(dog_age)]
