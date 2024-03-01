import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (23, 23, [1, 1]),
            (28, 29, [3, 3]),
            (27, 28, [2, 2]),
        ],
        ids=["cat dog age 0",
             "cat dog age 14",
             "cat dog age 23",
             "cat dog age 28 29",
             "cat dog age 27 28",
             ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected: list,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected
