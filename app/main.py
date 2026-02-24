def get_human_age(cat_age: int, dog_age: int) -> list:
    result = []
    result.append(check_age(cat_age, step=4))
    result.append(check_age(dog_age, step=5))
    return result


def check_age(age: int, step: int) -> int:
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0:
        raise ValueError("age cannot be negative")
    result = 0
    if age < 15:
        return result
    if age >= 15:
        result += 1
    if age >= 24:
        result += 1
        age -= 24
        if age > 0:
            result += age // step
    return result
