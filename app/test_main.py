import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                0, 0, [0, 0],
                id="return is 0 when inputs are 0"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="14 equals 0 for both"
            ),
            pytest.param(
                -29, 29, [0, 3],
                id="return 0 when age is negative"

            ),
            pytest.param(
                15, 15, [1, 1],
                id="return 1, when animal age is 15"

            ),
            pytest.param(
                23, 23, [1, 1],
                id="test 23 for both equals 1"
            ),

            pytest.param(
                25, 25, [2, 2],
                id="return 2 when age > 24"
            ),
            pytest.param(
                27, 29, [2, 3],
                id="test 27 of cat equals 2 and dog 29 equals 3"
            ),
            pytest.param(
                30, 30, [3, 3],
                id="returns 3 if age > 28"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="different human age of dog and cat at 28 years"
            ),
            pytest.param(
                45, 45, [7, 6],
                id="different age of cat and dog with big age"
            ),
            pytest.param(1000, 1000, [246, 197],
                         id="test working with big numbers")
        ]
    )
    def test_age(self,
                 cat_age: int,
                 dog_age: int,
                 expected: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    def test_type_of_value(self) -> None:
        with pytest.raises(Exception):
            get_human_age("cat", 4)
