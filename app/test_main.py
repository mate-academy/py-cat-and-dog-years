from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_years",
        [
            pytest.param(
                100,
                100,
                [21, 17],
                id="dog and cat years > 24 return correct human years"
            ),
            pytest.param(
                -1,
                0,
                [0, 0],
                id="dog and cat years <= 0 return [0, 0]"
            ),
            pytest.param(
                14,
                23,
                [0, 1],
                id="dog and cat years > 0 "
                   "and dog and cat years > 15 < 24 return [0, 1]"
            )
        ]
    )
    def test_cat_and_dog_age_to_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_years: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_years

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "12",
                12,
                TypeError,
                id="raise TypeError when years are not int")
        ]
    )
    def test_raising_correct_errors(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
