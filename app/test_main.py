import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age,expected_result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ]
    )
    def test_expected_age(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_result: list,
    ) -> None:
        assert (get_human_age(initial_cat_age, initial_dog_age)
                == expected_result)

    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age,expected_error",
        [
            ("text", 16, TypeError),
            (20, "text", TypeError),
        ]
    )
    def test_raising_error(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_error: TypeError,
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(initial_cat_age, initial_dog_age)
