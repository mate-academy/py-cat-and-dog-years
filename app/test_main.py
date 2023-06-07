import pytest

from typing import Any
from app.main import get_human_age


class TestGetHumanAgeResultCorrected:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return 0 if age is less than 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return 1 if 14 < age < 24"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id=("should return 2 if "
                    "23 < age < 28 for cat"
                    "and 23 < age < 29 for dog")
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id=("should return >= 3 if cat age >= 28"
                    "and >= 3 if dog age >= 29")
            ),
            pytest.param(
                -5,
                -100,
                [0, 0],
                id="checking for negative values"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="checking for null values"
            )
        ]
    )
    def test_result_corrected(
            self,
            cat_age: int,
            dog_age: int,
            result: list[int]
    ) -> None:

        assert get_human_age(cat_age, dog_age) == result


class TestErrorGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "",
                10,
                TypeError,
                id="wrong argument type for cat"
            ),
            pytest.param(
                5,
                [],
                TypeError,
                id="wrong argument type for dog"
            )
        ]
    )
    def test_wrong_argument(
            self,
            cat_age: Any,
            dog_age: Any,
            expected_error: TypeError
    ) -> None:

        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
