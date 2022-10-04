def get_human_age(cat_age, dog_age):
    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(animal_age, first_year, second_year, each_year):
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year



print(get_human_age(0, 0)) == [0, 0]
print(get_human_age(14, 14)) == [0, 0]
print(get_human_age(15, 15)) == [1, 1]
print(get_human_age(23, 23)) == [1, 1]
print(get_human_age(24, 24)) == [2, 2]
print(get_human_age(27, 27)) == [2, 2]
print(get_human_age(28, 28)) == [3, 2]
print(get_human_age(100, 100)) == [21, 17]