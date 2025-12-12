from app.main import get_human_age
import pytest
from typing import Any


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years,dog_years,expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return [0, 0]  when values are 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return [0, 0] when values less then 15"
            ),
            pytest.param(
                -2,
                -4,
                [0, 0],
                id="should return [0, 0] when values less then zero"
            )
        ]
    )
    def test_should_return_zeros(
            self,
            cat_years: int,
            dog_years: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected_result

    @pytest.mark.parametrize(
        "cat_years,dog_years,expected_result",
        [
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return 1 when > 14 and < 24"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return 1 when > 14 and < 24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return 2 when > 23 and < 28"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should return 2 when > 23 and < 28"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return 3 only for cat when > 27 and < 32"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="should return 3 for dog when > 28 and < 35"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should count properly for cat and dog"
            )
        ]
    )
    def test_should_return_correct_values(
            self,
            cat_years: int,
            dog_years: int,
            expected_result: int
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected_result

    @pytest.mark.parametrize(
        "cat_years, dog_years",
        [
            (None, None),
            ({"cat_years": 10}, {"dog_years": 10}),
            ((1,), (1,)),
            ([1, ], [2, ])
        ]
    )
    def test_should_raise_correct_error(
            self,
            cat_years: Any,
            dog_years: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_years, dog_years)
