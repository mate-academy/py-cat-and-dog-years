from __future__ import annotations

from app.main import get_human_age
import pytest


class TestGetHumanAgeFunction:
    @pytest.mark.parametrize(
        "cat_age_int,dog_age_int,expected_result_list",
        [
            pytest.param(-1000, -1000, [0, 0],
                         id="Negative age should return zeroes human ages"),
            pytest.param(14, 14, [0, 0],
                         id="Should return zeroes human ages"),
            pytest.param(15, 15, [1, 1],
                         id="Should return ones human ages"),
            pytest.param(23, 23, [1, 1],
                         id="Should return ones human ages"),
            pytest.param(24, 24, [2, 2],
                         id="Should return twos human ages"),
            pytest.param(27, 28, [2, 2],
                         id="Should return twos human ages"),
            pytest.param(28, 29, [3, 3],
                         id="Should return threes human ages"),
            pytest.param(31, 33, [3, 3],
                         id="Should return threes human ages"),
            pytest.param(32, 34, [4, 4],
                         id="Should return fours human ages"),
            pytest.param(35, 38, [4, 4],
                         id="Should return fours human ages"),
            pytest.param(4024, 5024, [1002, 1002],
                         id="Should return centuries human ages")
        ]
    )
    def test_can_get_human_age(self,
                               cat_age_int: int,
                               dog_age_int: int,
                               expected_result_list: list[int]) -> None:
        assert get_human_age(cat_age_int,
                             dog_age_int) == expected_result_list,\
            f"Should return {expected_result_list}"

    @pytest.mark.parametrize(
        "cat_age_int,dog_age_int,expected_result_error",
        [
            pytest.param("24", 56, TypeError,
                         id="Should raise TypeError when any arg is str"),
            pytest.param([24], 56, TypeError,
                         id="Should raise TypeError when any arg is list"),
            pytest.param({24: "4"}, 56, TypeError,
                         id="Should raise TypeError when any arg is dict"),
            pytest.param({24}, 56, TypeError,
                         id="Should raise TypeError when any arg is set"),
            pytest.param((24,), 56, TypeError,
                         id="Should raise TypeError when any arg is set"),
        ]
    )
    def test_can_get_human_age_error(self,
                                     cat_age_int: int,
                                     dog_age_int: int,
                                     expected_result_error: TypeError) -> None:
        with pytest.raises(expected_result_error):
            get_human_age(cat_age_int, dog_age_int)
