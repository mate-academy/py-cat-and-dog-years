import pytest

from app.main import get_human_age

# write your code here


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("2", "4"),
            ((2,), (4,)),
            ({2}, {4}),
            ([2], [4]),
            (None, None)
        ]
    )
    def test_correct_value_types_get_human_age(
            self, cat_age: int, dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_value",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
            (-3, -3, [0, 0])
        ],
        ids=[
            "0 animal years should be equal to 0 human year",
            "0 animal years should be equal to 0 human year",
            "15 animal years should be equal to 1 human year",
            "24 animal years should be equal to 2 human years",
            "23 animal years should be equal to 1 human year",
            "27/28 cat/dog years should be equal to 2 human years",
            "28/29 cat/dog years should be equal to 3 human years",
            "function should work with large numbers",
            "less than 0 cat/dog years should be equal to 0 human years"
        ]
    )
    def test_convert_ages_correctly(
        self, cat_age: int, dog_age: int, expected_value: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_value
