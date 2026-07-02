import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "dog_age, cat_age, expected_list",
        [
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (100, 100, [21, 17]),
            (0, 0, [0, 0]),
            (129847918247, 123771892361, [32_461_979_557, 24_754_378_469]),
            (-1, -26, [0, 0])
        ]
    )
    def test_function_get_humane_age(
            self,
            dog_age: int,
            cat_age: int,
            expected_list: list
    ) -> None:
        assert get_human_age(dog_age, cat_age) == expected_list

    @pytest.mark.parametrize(
        "dog_age, cat_age, expected_error",
        [
            ([0, 15], "dog", TypeError)
        ]
    )
    def test_raising_error(
            self,
            dog_age: int,
            cat_age: int,
            expected_error: type[TypeError]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(dog_age, cat_age)
