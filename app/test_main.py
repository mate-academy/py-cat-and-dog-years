from __future__ import annotations
import pytest
from app.main import get_human_age


class TestCatAndDogToHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            (0, 0, [0, 0]),
            (-1, -1, [0, 0]),
            (10, 10, [0, 0]),
            (10.5, 10.5, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (15.1, 15.1, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (25, 25, [2, 2]),
            (28, 28, [3, 2]),
            (29, 29, [3, 3]),
            (500, 500, [121, 97]),
        ],
        ids=[
            "function should return zeros for zero arguments",
            "function should return zeros for negative arguments",
            "function should works with first year for dogs and cats",
            "function should works with float numbers",
            "function should works with boarder parameters",
            "function should works with second year for dogs and cats",
            "function should works with float second year for dogs and cats",
            "function should works with min second year for dogs and cats",
            "function should works with max second year for dogs and cats",
            "function should works with second year for dogs and cats",
            "function should works with each year for cats",
            "function should works with each year for dogs",
            "function should works with big numbers",
        ]
    )
    def test_results_should_be_qual_to(
            self,
            cat_age: int | float,
            dog_age: int | float,
            result: list[int | float]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result


class TestTypesOfParameters:
    def test_type_error_for_parameters(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(1, "1")
