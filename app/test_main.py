import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            (
                0,
                0,
                [0, 0]
            ),
            (
                12,
                14,
                [0, 0]
            ),
            (
                24,
                27,
                [2, 2]
            ),
            (
                28,
                15,
                [3, 1]
            ),
            (
                54,
                97,
                [9, 16]
            ),
            (
                23,
                23,
                [1, 1]
            )
        ]
    )
    def test_to_count_a_human_age(
        self,
        cat_age: int,
        dog_age: int,
        human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age
