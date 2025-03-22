from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (29, 29, [3, 3]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "should return zero if years 0.",
            "animals years less 15 return 0.",
            "first 15 animals years give 1 human year.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27 cat/dog years should convert into 2 human age.",
            "28 cat years should convert into 3 human age.",
            "29 cat/dog years should convert into 3 human age.",
            "100 cat/dog years should convert into 21/17 human ages.",
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected
