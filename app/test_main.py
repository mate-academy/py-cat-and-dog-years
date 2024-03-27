from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            (0, 0, [0, 0]),
            (-1, -1, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ],
        ids=[
            "0 cat/dog years should convert into 0 human age.",
            "negative numbers should convert into 0 human age.",
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27 cat/dog years should convert into 2 human age.",
            "28 cat/dog years should convert into [3, 2] human age.",
            "100 cat/dog years should convert into [21, 17] human age.",
        ]
    )
    def test_valid_values(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_input,dog_input,expected_error",
        [
            ("cat", "dog", TypeError),
            (["a"], {1: "b"}, TypeError)
        ],
        ids=[
            "string arguments should raise TypeError",
            "list and dict arguments should raise TypeError"
        ]
    )
    def test_incorrect_types(
            self,
            cat_input: any,
            dog_input: any,
            expected_error: type[Exception]) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_input, dog_input)
