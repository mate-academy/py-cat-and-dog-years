import pytest
from typing import Any

from app.main import get_human_age


class TestConvertAge:
    @pytest.mark.parametrize(
        "animals_age,human_age",
        [
            ((-2, -2), [0, 0]),
            ((0, 0), [0, 0]),
            ((14, 14), [0, 0]),
            ((15, 15), [1, 1]),
            ((23, 23), [1, 1]),
            ((24, 24), [2, 2]),
            ((27, 28), [2, 2]),
            ((28, 29), [3, 3])
        ],
        ids=[
            "takes a negative value cat/dog"
            " years should convert into 0 human age",
            "0 cat/dog years should convert into 0 human age",
            "14 cat/dog years should convert into 0 human age",
            "15 cat/dog years should convert into 1 human age",
            "23 cat/dog years should convert into 1 human age",
            "24 cat/dog years should convert into 2 human age",
            "27/28 cat/dog years should convert into 2 human age",
            "28/29 cat/dog years should convert into 3 human age"
        ]
    )
    def test_cat_dog_years_should_convert_into_human_age(
            self,
            animals_age: tuple,
            human_age: list
    ) -> None:
        assert get_human_age(*animals_age) == human_age

    @pytest.mark.parametrize(
        "animals_age,expected_error",
        [
            (("19", "18"), TypeError),
        ],
        ids=[
            "should raise TypeError if takes string values",
        ]
    )
    def test_should_raise_error_if_takes_string_values(
            self,
            animals_age: tuple,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(*animals_age)
