def count_age(pet_age: int, *args) -> int:
    count_pet_age = 0
    counter = 0
    first, second, third = args

    for age in range(1, pet_age + 1):
        counter += 1

        if counter == first and count_pet_age == 0:
            count_pet_age += 1
            counter = 0

        if counter == second and count_pet_age == 1:
            count_pet_age += 1
            counter = 0

        if counter == third and count_pet_age > 1:
            count_pet_age += 1
            counter = 0

    return count_pet_age


def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_result = count_age(cat_age, 15, 9, 4)
    dog_result = count_age(dog_age, 15, 9, 5)

    # TODO: Implement this function
    # Write your tests first, then implement the logic
    return [cat_result, dog_result]
