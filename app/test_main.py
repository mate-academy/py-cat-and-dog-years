import pytest
from typing import Any
from app.main import get_human_age
from random import randrange


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, excepted_list",
        [
            pytest.param(
                randrange(0, 14),
                randrange(0, 14),
                [0, 0],
                id="must return [0, 0] when both ages are less than 15"
            ),
            pytest.param(
                randrange(15, 23),
                randrange(15, 23),
                [1, 1],
                id="must return [1, 1] when both ages in range 15-23"
            ),
            pytest.param(
                27, 28, [2, 2],
                id="must return [2, 2] human years"
            ),
            pytest.param(
                30, 29, [3, 3],
                id="must return [3, 3] human years"
            )

        ]

    )
    def test_worked_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            excepted_list: list[int, int]) -> None:
        assert get_human_age(cat_age, dog_age) == excepted_list


class TestGetHumanAgeExceptions:
    @pytest.mark.parametrize(
        "cat_age, dog_age, exception",
        [
            pytest.param(
                "1", "10", TypeError,
                id="invalid output should raises TypeError"
            )
        ]
    )
    def is_raise_error(self,
                       cat_age: int,
                       dog_age: int,
                       exception: Any) -> None:
        with pytest.raises(exception):
            get_human_age(cat_age, dog_age)
