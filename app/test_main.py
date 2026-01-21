import pytest
from app.main import get_human_age
from typing import Any


class TestAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(
                28, 28,
                [3, 2],
                id="test check that it is not changed with previous value"
            ),
            pytest.param(
                -1, 0,
                [0, 0],
                id="test receives data out of normal range"
            ),
            pytest.param(
                1000, 0,
                [246, 0],
                id="test receives data of large numbers"
            ),
            pytest.param(
                25.5, 45.1,
                [2, 6],
                id="test receives an float type of data"
            )
        ]
    )
    def test_get_human_age(
            self,
            cat_age: float,
            dog_age: float,
            expected: list,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                "15", 1, TypeError,
                id="test receives an str type of data"
            ),
            pytest.param(
                [], 1, TypeError,
                id="test receives an list type of data"
            ),
            pytest.param(
                {}, 1, TypeError,
                id="test receives an dict type of data"
            ),
            pytest.param(
                (), 1, TypeError,
                id="test receives an set type of data"
            )
        ]
    )
    def test_get_human_age_errors(
            self,
            cat_age: Any,
            dog_age: Any,
            expected_error: Any,
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
