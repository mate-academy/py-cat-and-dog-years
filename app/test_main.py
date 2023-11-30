import pytest

from app.main import get_human_age


class TestCatDog:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(
                -1, -1, [0, 0],
                id="Negative value"
            ),
            pytest.param(
                0, 0, [0, 0],
                id="Value is zero"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="Age less one"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="Age is one"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="Age not more than one"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="Age is two"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="Age not more than two"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="Different age for cat and dog"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="Age is one hundred"
            )
        ]
    )
    def test_cat_and_dog_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age_value, dog_age_value, expected",
        [
            pytest.param(
                None, 15, TypeError,
                id="Age is None"
            ),
            pytest.param(
                15, "m", TypeError,
                id="Age is not integer"
            )
        ]
    )
    def test_value_cat_and_dog(
            self,
            cat_age_value: int,
            dog_age_value: int,
            expected: tuple
    ) -> None:
        with pytest.raises(expected):
            get_human_age(cat_age_value, dog_age_value)
