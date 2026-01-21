from app.main import get_human_age
import pytest
from typing import Any


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="return when age is zero"),
            pytest.param(
                15, 15, [1, 1],
                id="return after first 15 years"),
            pytest.param(
                23, 23, [1, 1],
                id="return  until years 24 "),
            pytest.param(
                24, 24, [2, 2],
                id="return from years 24"),
            pytest.param(
                28, 29, [3, 3],
                id="return  for cat from years 28, for dog from years 29"),
            pytest.param(
                100, 100, [21, 17],
                id="return for years 100"),
        ])
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected_result: list
                           ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            pytest.param(
                "3", "5"),
            pytest.param(
                [], []),
            pytest.param(
                {}, {}),
            pytest.param(
                (), (),
                id="should return error than values are incorrect type")
        ])
    def test_raising_error_correctly(self, cat_age: Any, dog_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
