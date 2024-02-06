import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (1, 1, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "less 15 cat and dog years give 0 human year",
            "less 15 cat and dog years give 0 human year",
            "first 15 cat and dog years give 1 human year",
            "from 15 to 23 cat and dog years give 1 more human year",
            "after 23 years every 4 next cat years give 1 extra human year",
            "after 23 years every 5 next dog years give 1 extra human year",
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list[int]
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected
