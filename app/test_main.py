import pytest
from typing import Type
from app.main import get_human_age


class TestGetHumanAge():
    @pytest.mark.parametrize(
        "cat_age,dog_age,convert_to_human",
        [
            pytest.param(
                -1,
                -5,
                [0, 0],
                id="input negative values"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="Check if don't have a cat, or dog"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="14 cat/dog years should convert into 0 human age"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="15 cat/dog years should convert into 1 human age"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human age"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="24 cat/dog years should convert into 2 human age"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="27 cat/dog years should convert into 2 human age"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="28 cat 28 dog years should convert into 3/2 human age"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="100 cat, 100 dog years should convert into 21/17 human age"
            )
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            convert_to_human: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == convert_to_human

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                "string_input",
                1,
                id="Input some string instead of integer"
            ),
            pytest.param(
                [1],
                1,
                id="Input some list instead of integer"
            ),
            pytest.param(
                (1,),
                1,
                id="Input some set instead of integer"
            ),
            pytest.param(
                {"string_input": 1},
                1,
                id="Input some dict instead of integer"
            ),
            pytest.param(
                None,
                None,
                id="Input some None instead of integer"
            ),
        ]
    )
    def test_argument_type(
            self,
            cat_age: object,
            dog_age: object,
            expected_error: Type[Exception] = TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
