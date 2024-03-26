import pytest
from typing import Type
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_ages",
        [
            pytest.param(
                -5, -5, [0, 0],
                id="should return zeros if age is negative"
            ),
            pytest.param(
                0, 0, [0, 0],
                id="should return zeros if age is 0"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return zeros if age is under 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return 1 if age is under 24"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should return 1 extra every 4 years "
                   "for cat and 5 years for dog"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should return the right ages with big numbers"
            )
        ]
    )
    def test_should_return_right_calculations(
            self,
            cat_age: int,
            dog_age: int,
            expected_ages: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_ages

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("5", [15], TypeError)
        ]
    )
    def test_should_raise_error_when_using_incorrect_type_data(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
