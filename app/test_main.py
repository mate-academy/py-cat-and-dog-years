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
            ),
            pytest.param(
                0,
                -3,
                [0, 0],
                id="should return zero when age less or equal to zero"
            ),
            pytest.param(
                10000,
                7000,
                [2496, 1397],
                id="should work correctly with very large input values"
            )

        ]
    )
    def test_age(
            self,
            dog_age: int,
            cat_age: int,
            humane_age: list[int]
    ) -> None:
        assert (
            get_human_age(dog_age, cat_age) == humane_age
        )

    @pytest.mark.parametrize(
        "dog_age,cat_age",
        [
            pytest.param(
                "14",
                14,
                id="should raise TypeError when age is string"
            ),
            pytest.param(
                [23],
                23,
                id="should raise TypeError when age is list"
            ),
            pytest.param(
                None,
                28,
                id="should raise TypeError when age is None"
            )
        ]
    )
    def test_age_exceptions(
            self,
            dog_age: int,
            cat_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(dog_age, cat_age)

