import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            (0, 0, [0, 0]),
            (15, 15, [1, 1]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ]
    )
    def test_animals_to_human(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result
