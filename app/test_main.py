import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="test return 0 if animal age equals 0",
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="test return 0 if animal age less than first year",
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="test return 1 if animal age equal first year",
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="test return 1 if less than sum first and second",
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="test return 2 if animal age equal sum 1 year and 2 year",
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="test return 2 if animal age equals 27",
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="test return 2 if animal age equals 28",
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="test return 2 if animal age equals 100",
            ),
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="test negative age",
            )
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected: list
                           ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                "cat_age",
                "dog_age",
                TypeError,
            )
        ]
    )
    def test_get_human_age_error(self,
                                 cat_age: str,
                                 dog_age: str,
                                 expected_error: TypeError
                                 ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
