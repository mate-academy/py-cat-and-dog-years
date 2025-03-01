import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age",
                         [
                             (0, 0),
                             (14, 14),
                             (15, 15),
                             (23, 23),
                             (24, 24),
                             (27, 27),
                             (28, 28),
                             (100, 100)
                         ]
                         )
class TestAnimalAgeToHumanAge:
    def test_less_then_15_years_is_0_human_year(
            self,
            cat_age: int,
            dog_age: int) -> None:
        if cat_age >= 15 and dog_age >= 15:
            pytest.skip("Only less than 15 years")
            return

        result = get_human_age(cat_age, dog_age)

        if cat_age < 15:
            assert result[0] == 0
        if dog_age < 15:
            assert result[1] == 0

    def test_first_15_years_is_1_human_year(
            self,
            cat_age: int,
            dog_age: int) -> None:
        if cat_age < 15 and dog_age < 15:
            pytest.skip("Only more than 15 years")
            return

        result = get_human_age(cat_age, dog_age)

        if 15 <= cat_age < 24:
            assert result[0] == 1
        if 15 <= dog_age < 24:
            assert result[1] == 1

    def test_next_9_years_is_1_more_human_year(
            self,
            cat_age: int,
            dog_age: int) -> None:
        if cat_age < 24 and dog_age < 24:
            pytest.skip("Only more than or equal 24 years")
            return

        result = get_human_age(cat_age, dog_age)

        if 24 <= cat_age < 28:
            assert result[0] == 2
        if 24 <= dog_age < 29:
            assert result[1] == 2

    def test_every_4_5_cat_dog_years_gives_1_extra_human_year(
            self,
            cat_age: int,
            dog_age: int) -> None:
        if cat_age < 28 and dog_age < 29:
            pytest.skip("Only when cat more then or equal 28 years"
                        " or dog more then or equal 29 years")
            return

        result = get_human_age(cat_age, dog_age)

        if cat_age >= 28:
            assert result[0] == 3 + (cat_age - 28) // 4
        if dog_age >= 29:
            assert result[1] == 3 + (dog_age - 29) // 5
