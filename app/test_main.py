import pytest
from typing import Any

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_age",
        [
            pytest.param(
                14, 14, [0, 0],
                id="return 0 human years for 14 cat/dog years",
            ),
            pytest.param(
                0, 0, [0, 0],
                id="return 0 human years for 0 cat/dog years",
            ),
            pytest.param(
                15, 23, [1, 1],
                id="return 1 human years for 15 cats and 23 dogs years",
            ),
            pytest.param(
                27, 28, [2, 2],
                id="return 2 human years for 27 cats and 28 dogs years",
            ),
            pytest.param(
                28, 28, [3, 2],
                id="return 3 and 2 human years for 28 cats/dogs year",
            ),
            pytest.param(
                100, 100, [21, 17],
                id="return 21 human years for cat and 17 for dogs 100 years",
            ),
        ]
    )
    def test_get_human_age_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int],
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "23", 23, TypeError,
                id="when we put incorect type for parameters"
            )
        ]
    )
    def test_get_human_age_with_errors(
        self,
        cat_age: Any,
        dog_age: Any,
        expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
