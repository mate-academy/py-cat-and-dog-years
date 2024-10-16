from app.main import get_human_age

import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,"
        "dog_age,"
        "human_age", [
            pytest.param(
                -17, -17,
                [0, 0],
                id="test less than 0 years cat dog"
                   "should convert in 0 human age"
            ),
            pytest.param(
                0, 0,
                [0, 0],
                id="test 0 years cat dog should convert in 0 human age"
            ),
            pytest.param(
                700, 700,
                [171, 137],
                id="test large numbers of years cat dog"
                   "should convert in 171, 137 human age"
            ),
            pytest.param(
                14, 14,
                [0, 0],
                id="test 14 years cat dog should convert in 0 human age"
            ),
            pytest.param(
                15, 15,
                [1, 1],
                id="test 15 years cat dog should convert in 1 human age"
            ),
            pytest.param(
                23, 23,
                [1, 1],
                id="test 23 years cat dog should convert in 1 human age"
            ),
            pytest.param(
                24, 24,
                [2, 2],
                id="test 24, 24 years cat dog should convert in 2 human age"
            ),
            pytest.param(
                27, 28,
                [2, 2],
                id="test 27, 28 years cat dog should convert in 2 human age"
            ),
            pytest.param(
                28, 29,
                [3, 3],
                id="test 28, 29 years cat dog should convert in 3 human age"
            )
        ]
    )
    def test_should_convert_cat_dog_age_to_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: int
    ) -> None:

        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age,"
        "dog_age,"
        "expected_error", [
            pytest.param(
                "20", "20",
                TypeError,
                id="test should raising Type Error"
            )
        ]
    )
    def test_raising_errors_in_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: type
    ) -> None:

        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
