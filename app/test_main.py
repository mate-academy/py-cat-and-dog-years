from app.main import get_human_age
import pytest


class TestCatAndDogeAge:
    @pytest.mark.parametrize(
        "dog_age,cat_age,humane_age",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return zero when age less then 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return one year when age less then 24"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="should return two years when age equal 27 and 28"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="should return tree years when age equal 28 and 29"
            )
        ]
    )
    def test_age(self, dog_age: int, cat_age: int, humane_age: list) -> None:
        assert (
            get_human_age(dog_age, cat_age) == humane_age
        )
