import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            (28, 100, [3, 17]),
            (27, 28, [2, 2]),
            (100, 33, [21, 3]),
            (0, -100, [0, 0]),
            (10 ** 5, 10 ** 5, [24996, 19997]),
        ],
        ids=[
            "should return values in human age",
            "should not increase human cat age before 28 years",
            "should not increase human dog age before 34 years",
            "should not increase value if one of the value are <= 0",
            "should work correctly with large numbers",
        ],
    )
    def test_get_human_age(
        self,
        cat_age: int,
        dog_age: int,
        expected_result: list[int],
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("32", 25, TypeError)
        ],
        ids=[
            "should raise `TypeError` exception",
        ],
    )
    def test_type_of_data(
        self,
        cat_age: str,
        dog_age: int,
        expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
