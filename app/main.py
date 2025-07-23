def get_human_age(cat_years, dog_years):
    def convert(years, first, second, each):
        if years < first:
            return 0
        elif years < first + second:
            return 1
        else:
            return 2 + (years - first - second) // each

    cat_human = convert(cat_years, 15, 9, 4)
    dog_human = convert(dog_years, 15, 9, 5)
    return [cat_human, dog_human]

