import pytest

from app.main import get_human_age


class TestCatAndDogYears:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="0 cat or dog years should convert to 0 human years"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="14 cat or dog years should convert to 0 human years"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="15 cat or dog years should convert to 1 human year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat or dog years should convert to 1 human year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="24 cat or dog years should convert to 2 human years"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="27 cat or dog years should convert to 2 human years"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id=("28 cat years should convert to 3 human "
                    "years, but not dog's")
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id=("100 cat years should convert to 21 human years, "
                    "and 100 dog years should convert to 17 human years")
            ),
        ]
    )
    def test_cat_and_dog_years(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result


class TestTypes:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "15",
                0,
                TypeError,
                id="you can only pass 'int' type for age"
            ),
            pytest.param(
                14,
                [14],
                TypeError,
                id="you can only pass 'int' type for age"
            ),
            pytest.param(
                15,
                {15},
                TypeError,
                id="you can only pass 'int' type for age"
            )
        ]
    )
    def test_cat_and_dog_correct_types(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
