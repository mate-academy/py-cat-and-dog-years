import pytest
from app.main import get_human_age


class TestAgeCheck:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                -11, -11,
                [0, 0],
                id="human age must be 0 if pet age is negative"
            ),
            pytest.param(
                0, 0,
                [0, 0],
                id="human age must be 0 if pet age is 0"
            ),
            pytest.param(
                14, 14,
                [0, 0],
                id="14 years of cat/dog age should convert into 0 human age"
            ),
            pytest.param(
                15, 15,
                [1, 1],
                id="15 years of cat/dog age should convert into 1 human age"
            ),
            pytest.param(
                23, 23,
                [1, 1],
                id="23 years of cat/dog age should convert into 1 human age"
            ),
            pytest.param(
                24, 24,
                [2, 2],
                id="24 years of cat/dog age should convert into 1 human age"
            ),
            pytest.param(
                27, 28,
                [2, 2],
                id="27, 28 years of cat/dog age should convert into 2 human age"
            ),
            pytest.param(
                28, 29,
                [3, 3],
                id="28, 29 years of cat/dog age should convert into 3 human age"
            ),
            pytest.param(
                100, 100,
                [21, 17],
                id="100 years of cat/dog age should convert into 21/17 human age."
            ),
        ]
    )
    def test_get_human_ages(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result
