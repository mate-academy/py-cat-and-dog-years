import pytest

from app.main import get_human_age, AgeError


class TestConvertCatDogAges:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should get human age when catdog ages are 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should get human age when catdog ages are 14"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should get human age when catdog ages are 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should get human age when catdog ages are 23"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should get human age when catdog ages are 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should get human age when catdog ages are 27"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should get human age when catdog ages are 28"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should get human age more then 24 catdog ages"
            )
        ]
    )
    def test_convert_cat_dog_ages(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestWrongInput:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                -1,
                -2,
                ValueError,
                id="negative animal age input"
            ),
            pytest.param(
                155,
                270,
                AgeError,
                id="tolong animal age"
            )

        ]
    )
    def test_raisin(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: BaseException
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
