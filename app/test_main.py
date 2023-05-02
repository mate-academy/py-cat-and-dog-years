import pytest

from typing import Any

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="cat/dog years should convert into 3/2 human age."
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="cat/dog years should convert into 21/17 human age."
            ),
            pytest.param(
                -10,
                -10,
                [0, 0],
                id="check function for negative values"
            ),
        ]
    )
    def test_cat_and_dog_age_convert_to_human(
            self,
            cat_age: int,
            dog_age: int,
            result: list,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age, dog_age, error",
        [
            pytest.param(
                "1",
                "1",
                TypeError,
                id="value should be int. Not string!"
            ),
            pytest.param(
                [1],
                [1],
                TypeError,
                id="value should be int. Not list!"
            ),
        ])
    def test_animal_age_wrong_values(
            self,
            cat_age: Any,
            dog_age: Any,
            error: TypeError
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
