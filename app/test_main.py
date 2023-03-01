import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_list",
        [
            (0, -1, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2])
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_list: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_list


def test_receives_an_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 13.5)
