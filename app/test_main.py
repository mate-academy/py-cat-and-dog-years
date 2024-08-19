import pytest

from app.main import get_human_age


class TestAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (-2, -3, [0, 0]),
            (-2, 3, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (100, 100, [21, 17])
        ],
        ids=[
            "Both cat and dog age 0 should result in [0, 0] human years",
            "Negative cat and dog ages should result in [0, 0] human years",
            "Negative cat age and 3 dog years should result in [0, 0] human years",
            "14 cat and dog years should result in [0, 0] human years",
            "15 cat and dog years should result in [1, 1] human years",
            "23 cat and dog years should result in [1, 1] human years",
            "24 cat and dog years should result in [2, 2] human years",
            "100 cat and dog years should result in [21, 17] human years"
        ]
    )
    def test_get_human_age(self, cat_age: int, dog_age: int, expected: int) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    def test_type_errors(self) -> None:
        with pytest.raises(TypeError):
            assert get_human_age("cat_age", "dog_age")
