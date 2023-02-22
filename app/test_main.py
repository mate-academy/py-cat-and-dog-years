import pytest


from app.main import get_human_age


class TestCatsAndDogsHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ],
        ids=[
            "check cubs",
            "check right before first birthday",
            "check right after first birthday",
            "check right before second birthday",
            "check right after second birthday",
            "check age difference",
            "check old timers"
        ]
    )
    def test_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list) -> None:
        assert get_human_age(cat_age, dog_age) == human_age
