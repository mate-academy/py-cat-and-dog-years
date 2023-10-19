from __future__ import annotations
import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                -20,
                -30,
                [0, 0],
                id="should return [0, 0] when cat age = -20 and dog age = -30"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return [0, 0] when cat age = 0 and dog age = 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return [0, 0] when cat age = 14 and dog age = 14"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return [1, 1] when cat age = 15 and dog age = 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return [1, 1] when cat age = 23 and dog age = 23"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return [2, 2] when cat age = 24 and dog age = 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should return [2, 2] when cat age = 27 and dog age = 27"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return [3, 2] when cat age = 28 and dog age = 28"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return [21, 17] when cat age = 100, dog age = 100"
            )
        ]
    )
    def test_calculates_age_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    def test_should_raise_type_error_when_parameter_not_integer(self) -> None:
        with pytest.raises(TypeError):
            assert get_human_age("10", "10")
