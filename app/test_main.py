import pytest
from app.main import get_human_age


def test_should_return_list() -> None:
    assert isinstance(get_human_age(10, 10), list)


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="func get zero"
            ),
            pytest.param(
                -1,
                -5,
                [0, 0],
                id="func get negative numbers"
            ),
            pytest.param(
                300,
                300,
                [71, 57],
                id="func get large numbers"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="14 cat and dog years should equals 0 human age"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat and dog years should equals 1 human age"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="27 cat and 28 dog years should equals 2 human age"
            )
        ]
    )
    def test_check_correctness_function_result(
        self,
        cat_age: int,
        dog_age: int,
        result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result
