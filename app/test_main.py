import pytest
from app.main import get_human_age


class TestIntValues:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (-1, -12, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (16, 16, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (29, 41, [3, 5]),
            (14.6, 18.7, [0, 1]),
            (23.6, 23.9, [1, 1]),
            (6, 61, [0, 9]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (100_000_000, 100_000_021, [24_999_996, 20_000_001]),
        ],
        ids=[
            "cat-0-dog-0",
            "cat-'-1'-dog-'-12'",
            "cat-14-dog-14",
            "cat-15-dog-15",
            "cat-16-dog-16",
            "cat-23-dog-23",
            "cat-24-dog-24",
            "cat-27-dog-27",
            "cat-29-dog-41",
            "cat-14.6-dog-18.7",
            "cat-23.5-dog-23.9",
            "cat-6-dog-61",
            "cat-28-dog-28",
            "cat-100-dog-100",
            "cat-100 000 000-dog-100 000 021"

        ]
    )
    def test_modify_animals_age_correctly(
            self, cat_age: int, dog_age: int, expected: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestFaultValues:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ([21], "12"),
            ([], {}),
            (None, None),
        ],
    )
    def test_not_int_values(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
