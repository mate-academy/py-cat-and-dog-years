import pytest

from app.main import get_human_age


class TestCountAges:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return list with zeroes"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return zeroes when age less then 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return one when age less then 23 but >= 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return two human years when age is more or equal 24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return [2, 2] when cat/dog age is 24.9/27.9"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should return 3/2 cat/dog when their age is 28/28"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return 3/2 cat/dog when their age is 28/28"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="shuld count correctly when cat/dog age is 100/100"
            ),
            pytest.param(
                1000,
                1000,
                [246, 197],
                id="should work correctly when age is very large number"
            ),
            pytest.param(
                -5,
                -20,
                [0, 0],
                id="should return zeroes when age is negative number"
            )
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                [1],
                [100],
                TypeError,
                id="should raise TypeError exception when cat/dog age is list"
            ),
            pytest.param(
                "2",
                "3",
                TypeError,
                id="should raise TypeError exception when cat/dog age is str"
            ),
            pytest.param(
                {13},
                {19},
                TypeError,
                id="should raise TypeError exception when cat/dog age is dict"
            )
        ]
    )
    def test_func_raises_correct_error(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
