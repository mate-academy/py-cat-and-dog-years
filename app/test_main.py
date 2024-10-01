import pytest
from app.main import get_human_age


class TestAnimalAge:
    @pytest.mark.parametrize(
        "age_cat, age_dog, expected_result",
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
    def test_check_age_for_cat_and_dog_in_human_age(
            self,
            age_cat: int,
            age_dog: int,
            expected_result: list
    ) -> None:

        assert get_human_age(age_cat, age_dog) == expected_result

    @pytest.mark.parametrize(
        "age_cat, age_dog, expected_exception",
        [
            (-100, -200.05, ValueError),
            (311232321, 323123215, ValueError),
            ("311232321", 22, TypeError)
        ]
    )
    def test_invalid_inputs(
            self,
            age_cat: int,
            age_dog: int,
            expected_exception: Exception
    ) -> None:
        with pytest.raises(expected_exception):
            get_human_age(age_cat, age_dog)
