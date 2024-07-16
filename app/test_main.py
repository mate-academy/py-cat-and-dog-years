import pytest
from app.main import get_human_age


class TestAllWorkCorrectly:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_age",
        [
            (0, 0, [0, 0]),
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
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27 cat/dog years should convert into 2 human age.",
            "28 cat/dog years should convert into 3/2 human age.",
            "100 cat/dog years should convert into 21/17 human age.",

        ]
    )
    def test_should_check_all_values(
            self,
            cat_age: int,
            dog_age: int,
            expected_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("string", 15, TypeError),
            (31, "string", TypeError),
            ("string", "string", TypeError)
        ],
        ids=[
            "should raise error if cat_age is not an integer",
            "should raise error if dog_age is not an integer",
            "should raise error if cat_age and dog_age are not integers"
        ]
    )
    def test_should_raise_error(
            self,
            cat_age: int,
            dog_age: int,
            expected_error
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
