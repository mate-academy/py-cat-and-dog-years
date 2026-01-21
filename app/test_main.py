from typing import Any

import pytest

from app.main import get_human_age


class TestHumanAgeConversion:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (-1, -100, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100.001, 100, [21, 17])
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected_result: list[int]) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            pytest.param(None, None,
                         id="`None` should raise `TypeError`"),
            pytest.param("10", "10",
                         id="`str` should raise `TypeError`"),
            pytest.param({1, 2}, {1, 2},
                         id="`set` should raise `TypeError`")
        ]
    )
    def test_test_get_human_age_errors(
            self,
            cat_age: Any,
            dog_age: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
