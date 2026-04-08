from app.main import get_human_age
import pytest


class TestCheckAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_res",
        [
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3]),
            (0, 0, [0, 0]),
            (-20, -30, [0, 0]),
            (100, 100, [21, 17])
        ]
    )
    def test_check_correct_return(
        self,
        cat_age: int,
        dog_age: int,
        expected_res: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_res

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            ("0", "14", TypeError)
        ]
    )
    def test_get_errors(
        self,
        cat_age: int,
        dog_age: int,
        expected_error: type
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
