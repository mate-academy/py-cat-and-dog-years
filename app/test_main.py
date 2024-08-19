import pytest

from app.main import get_human_age


class TestAge:
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
            (100, 100, [21, 17])
        ],
        ids=[
            "0 cat and dog age must equal 0 in human age",
            "14 cat and dog years must equal 0 in human age",
            "15 cat and dog years must equal 1 in human age",
            "23 cat and dog years must equal 1 in human age",
            "24 cat and dog years must equal 2 in human age",
            "27 cat and dog years must equal 2 in human age",
            "28 cat and dog years must equal 3 and 2 in human age",
            "100 cat and dog years must equal 21 and 17 in human age"
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected: int) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    def test_type_errors(self) -> None:
        with pytest.raises(TypeError):
            assert get_human_age("cat_age", "dog_age")
