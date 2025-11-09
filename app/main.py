# main.py
def convert_to_human(age, first_year, second_year, each_year):
    if age < first_year:
        return 0
    elif age < first_year + second_year:
        return 1
    else:
        return 2 + int((age - (first_year + second_year)) / each_year)

def get_human_age(cat_age, dog_age):
    # Тут підставляються ті самі значення, що в тестах
    first_year = 15
    second_year = 9
    each_year_cat = 4
    each_year_dog = 5
    cat_h = convert_to_human(cat_age, first_year, second_year, each_year_cat)
    dog_h = convert_to_human(dog_age, first_year, second_year, each_year_dog)
    return [cat_h, dog_h]
