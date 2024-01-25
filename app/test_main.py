import pytest as pytest
from app.main import get_human_age
from typing import Any


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_age",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="less 15 cat/dog years give 0 human year;"
            ),
            pytest.param(
                14.9,
                14.6,
                [0, 0],
                id="less 15 cat/dog years give 0 human year;"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id=("if function resive data out of normal range,"
                    " such as negative numbers, zero, or realy large numbers;")
            ),
            pytest.param(
                -4,
                -454545,
                [0, 0],
                id=("if function resive data out of normal range,"
                    " such as negative numbers, zero, or realy large numbers;")
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="first 15 cat/dog years give 1 human year;"
            ),
            pytest.param(
                16,
                16,
                [1, 1],
                id="first 15 cat/dog years give 1 human year;"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="the next 9 cat years give 1 more human year;"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="the next 9 cat years give 1 more human year;"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="the next 9 cat years give 1 more human year;"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id=("every 4 next cat years give 1 extra human year"
                    "every 5 next dog years give 1 extra human year.")
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id=("every 4 next cat years give 1 extra human year"
                    "every 5 next dog years give 1 extra human year.")
            ),
        ]
    )
    def test_convert_to_human_age_correct(
            self,
            cat_age: int,
            dog_age: int,
            expected_human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "12",
                14,
                TypeError,
                id="should raise error if cat_age/dog_age is number"
            ),
            pytest.param(
                12,
                "12",
                TypeError,
                id="should raise error if cat_age/dog_age is number"
            ),
        ]
    )
    def test_rising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
