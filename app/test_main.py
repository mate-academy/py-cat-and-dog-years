import pytest

from app.main import get_human_age


class TestCatDogAge:

    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (25, 25, [2, 2]),
        (28, 29, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
        (-1, -5, [0, 0]),
    ],
        ids=[
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "25 cat/dog years should convert into 2 human age.",
            "28/29 cat/dog years should convert into 3 human age.",
            "32/34 cat/dog years should convert into 4 human age.",
            "cat/dog don't live for so long",
            "Negative cat/dog years should convert into 0 human age."
        ])
    def test_get_human_age(self, cat_age, dog_age, expected):
        assert get_human_age(cat_age, dog_age) == expected
