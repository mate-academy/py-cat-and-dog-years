import pytest

from typing import Any, Type

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="The negative years' value should convert into 0 human age."
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="0 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="14 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="15 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="24 cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="27/28 cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="28/29 cat/dog years should convert into 3 human age."
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="100 cat/dog years should convert into 21/17 human age."
            ),
        ]
    )
    def test_cat_and_dog_years_convert_to_human_age(
        self,
        cat_age: int,
        dog_age: int,
        result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                "15",
                15,
                TypeError,
                id="Should raise error if the year's value is not an integer."
            ),
            pytest.param(
                15,
                [15],
                TypeError,
                id="Should raise error if the year's value is not an integer."
            )
        ]
    )
    def test_raising_errors_in_wrong_type_cases(
        self,
        cat_age: Any,
        dog_age: Any,
        expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
