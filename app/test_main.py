import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                100,
                100,
                [21, 17],
                id="cat/dog > 24 return correct human years"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="cat/dog <= 0 return [0, 0]"
            ),
            pytest.param(
                14,
                23,
                [0, 1],
                id="cat/dog > 0 and cat/dog_age > 15 < 24 return [0, 1]"
            ),
        ]
    )
    def test_cat_and_dog_age_to_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "10",
                10,
                TypeError,
                id="raise TypeError whe years is not int"
            )
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
