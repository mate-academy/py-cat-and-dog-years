from app.main import get_human_age
import pytest


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
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
    )
    def test_should_check_return_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            (str, int),
            (int, str),
            (str, str),
            (None, int),
            (int, None),
            (None, None)
        ]
    )
    def test_should_accept_correct_types(
            self, cat_age: int, dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
