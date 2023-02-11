import pytest
from app.main import get_human_age


def test_should_return_list() -> None:
    years = get_human_age(0, 0)
    assert isinstance(years, list)


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                0, 0, [0, 0],
            ),
            pytest.param(
                14, 14, [0, 0],
            ),
            pytest.param(
                23, 23, [1, 1],
            ),
            pytest.param(
                28, 28, [3, 2],
            ),
            pytest.param(
                100, 100, [21, 17],
            ),
        ],
        ids=[
            "With animal age 0 should return [0, 0]",
            "With animal age before 15 should return [0, 0]",
            "With animal age before 23 and 23 should return [1, 1]",
            "With animal age before 28 and 28 should return [3, 2]",
            "With animal age before 100 and 100 should return [21, 17]",
        ]
    )
    def test_get_human_age(
            self, cat_age: int, dog_age: int, result: tuple
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result
