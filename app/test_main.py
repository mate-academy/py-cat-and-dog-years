import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (24, 24, [2, 2]),
            (100, 100, [21, 17])
        ],
        ids=[
            "zeros if zero",
            "almost a full year",
            "one full year precisely",
            "almost a second year",
            "two full years precisely",
            "both 24, so 3 and 2",
            "both 100, so 21 and 17"
        ]
    )
    def test_normal_arguments_and_zero(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (-1, -1)
        ],
        ids=[
            "Negative numbers as zeros"
        ]
    )
    def test_exception_raising(
            self,
            cat_age: int,
            dog_age: int,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == [0, 0]
