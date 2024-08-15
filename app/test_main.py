import pytest
from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
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
            "zero cats and dogs must equal 0 years in human age",
            "14 cat years and god years must equal 0 years in human age",
            "15 cat years and god years must equal 1 years in human age",
            "23 cat years and god years must equal 1 years in human age",
            "24 cat years and god years must equal 2 years in human age",
            "27 cat years and god years must equal 2 years in human age",
            "28 cat years and god years must equal 3, 2 years in human age",
            "100 cat years and god years must equal21, 17 years in human age"
        ]
    )
    def test_for_values(
            self,
            cat_age: int,
            dog_age: int,
            expected: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    def test_for_type_errors(self) -> None:
        with pytest.raises(TypeError):
            assert get_human_age("cat_age", "dog_age")
