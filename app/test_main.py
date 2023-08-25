import pytest

from app.main import get_human_age


class TestAnimalAge:
    @pytest.mark.parametrize(
        "dog_age, cat_age, result",
        [
            (
                100,
                100,
                [21, 17]
            ),
            (
                14,
                14,
                [0, 0]
            ),
            (
                23,
                23,
                [1, 1]
            ),
        ]
    )
    def test_dog_age(
            self,
            dog_age: int,
            cat_age: int,
            result: list[int]
    ) -> None:
        assert get_human_age(dog_age, cat_age) == result
