from app.main import get_human_age, convert_to_human


class Cat:
    def test_first_15_years_give_human_year(self):
        cat_age = 15
        human_age = convert_to_human(cat_age, 15, 9, 4)
        assert human_age == 1, f"Expected 1 human year for {cat_age} cat years, but got {human_age}"
        print("Test passed!")

    def test_next_9_years_give_1_more_human_year(self):
        cat_age = 25
        human_age = convert_to_human(cat_age, 15, 9, 4)
        assert human_age == 2, f"Expected 2 human year for {cat_age} cat years, but got {human_age}"
        print("Test passed!")

    def test_every_4_next_cat_years_give_extra_human_year(self):
        cat_age = 28  # 15 (first year) + 9 (second year) + 4
        human_age = convert_to_human(cat_age, 15, 9, 4)
        expected_human_age = 3  # 1 (first year) + 1 (second year) + 1 (for every 4 years after)
        assert human_age == expected_human_age, (f"Expected {expected_human_age} human "
                                                 f"years for {cat_age} cat years, but got {human_age}")
        print("Test passed!")

class Dog:
    def test_first_15_years_give_human_year(self):
        cat_age = 15
        human_age = convert_to_human(cat_age, 15, 9, 4)
        assert human_age == 1, f"Expected 1 human year for {cat_age} dog years, but got {human_age}"
        print("Test passed!")

    def test_next_9_years_give_1_more_human_year(self):
        dog_age = 25
        human_age = convert_to_human(dog_age, 15, 9, 4)
        assert human_age == 2, f"Expected 2 human year for {dog_age} dog years, but got {human_age}"
        print("Test passed!")

    def test_every_5_next_cat_years_give_extra_human_year(self):
        dog_age = 29  # 15 (first year) + 9 (second year) + 5
        human_age = convert_to_human(dog_age, 15, 9, 5)
        expected_human_age = 3  # 1 (first year) + 1 (second year) + 1 (for every 5 years after)
        assert human_age == expected_human_age, f"Expected {expected_human_age} human years for {dog_age} dog years, but got {human_age}"
        print("Test passed!")

