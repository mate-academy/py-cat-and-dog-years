import pytest
from typing import Any

from app.main import get_human_age


class TestConvertAge:
    @pytest.mark.parametrize(
        "cat_years,dog_years,list_of_human_ages",
        [
            pytest.param(0, 0, [0, 0], ),
            pytest.param(15, 15, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(28, 28, [3, 2]),
            pytest.param(100, 100, [21, 17])
        ]
    )
    def test_convert_to_human_age(
            self,
            cat_years: int,
            dog_years: int,
            list_of_human_ages: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == list_of_human_ages

    @pytest.mark.parametrize(
        "cat_years,dog_years,expected_error",
        [
            pytest.param(0, "1", TypeError),
            pytest.param("1", 0, TypeError),
            pytest.param([234, 32], 15, TypeError),
            pytest.param(24, [1243, 34, ], TypeError),
            pytest.param((32, 2), 28, TypeError),
            pytest.param(100, (12, 3), TypeError),
            pytest.param(100, {12: 12}, TypeError),
            pytest.param({123: 213}, 15, TypeError),
        ]
    )
    def test_with_wrong_types(
            self,
            cat_years: Any,
            dog_years: Any,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_years, dog_years)
