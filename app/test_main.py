from typing import List


def get_human_age(cat_age: int, dog_age: int) -> List[int]:
    # Валідація типів
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")
    # Валідація на непозитивність
    if cat_age < 0 or dog_age < 0:
        raise ValueError("cat_age and dog_age must be non-negative")

    def convert_cat_years(c_age: int) -> int:
        human_years = 0
        if c_age >= 15:
            human_years += 1
            c_age -= 15
            if c_age >= 9:
                human_years += 1
                c_age -= 9
                human_years += c_age // 4
            else:
                # якщо c_age < 9, не додаємо другого року і більше
                pass
        else:
            # якщо c_age < 15, не додаємо людських років
            pass
        return human_years

    def convert_dog_years(d_age: int) -> int:
        human_years = 0
        if d_age >= 15:
            human_years += 1
            d_age -= 15
            if d_age >= 9:
                human_years += 1
                d_age -= 9
                human_years += d_age // 5
            else:
                # якщо d_age < 9, не додаємо другого року і більше
                pass
        else:
            # якщо d_age < 15, не додаємо людських років
            pass
        return human_years

    return [convert_cat_years(cat_age), convert_dog_years(dog_age)]
