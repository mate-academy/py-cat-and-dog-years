import pytest

from app.main import get_human_age


class TestCatDogAge:
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
            (100, 100, [21, 17]),
        ],
        ids=[
            "0 cat/dog years should convert into 0 human age.",
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27/28 cat/dog years should convert into 2 human age.",
            "28/29 cat/dog years should convert into 3 human age.",
            "100/100 cat/dog years should convert into 21/17 human age.",
        ]
    )
    def test_expected(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    def test_type_error_for_parameters(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("1", 1)
