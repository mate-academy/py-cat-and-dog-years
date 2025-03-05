import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_value",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 29, [3, 3]),
            (50, 50, [8, 7]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "ages with zero values",
            "ages just below first human year",
            "ages at first human year threshold",
            "ages just below second human year",
            "ages at second human year threshold",
            "ages at third human year threshold",
            "ages with larger values",
            "ages at one hundred"
        ]
    )
    def test_correct_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_value: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_value

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param("", "one", TypeError)
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: type[BaseException]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
