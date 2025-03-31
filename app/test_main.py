import pytest
from _pytest.mark import ParameterSet

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cats_age, dogs_age, cat_human_age, dog_human_age,",
        [
            pytest.param(14, 14, 0, 0, id="animal years must be less than 1"),
            pytest.param(15, 15, 1, 1, id="animal years must be equals 1"),
            pytest.param(24, 24, 2, 2, id="animal years must be equals 2"),
            pytest.param(23, 23, 1, 1, id="animal years must be equals 1"),
            pytest.param(28, 29, 3, 3, id="animal years must be equals 3"),
            pytest.param(27, 28, 2, 2, id="animal years must be equals 3"),

        ]

    )
    def test_correctly_convert(
        self,
        cats_age: ParameterSet,
        dogs_age: ParameterSet,
        cat_human_age: ParameterSet,
        dog_human_age: ParameterSet
    ) -> None:
        assert get_human_age(cats_age, dogs_age) == [
            cat_human_age,
            dog_human_age
        ]
