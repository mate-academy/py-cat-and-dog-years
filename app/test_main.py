import pytest
from app.main import get_human_age


class TestConvertAge:
    @pytest.mark.parametrize(
        "age_for_dog, age_for_cat, expected_age_dog_cat", [
            pytest.param(
                -10,
                -10,
                [0, 0],
                id="Function should convert -10 to 0 for dog or cat"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="Function should convert 0 to 0 for dog or cat"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Function should convert 14 to 0 for dog or cat"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="Function should convert 15 to 1 for dog or cat"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="Function should convert 23 to 1 for dog or cat"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="Function should convert 24 to 2 for dog or cat"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="Function should convert 27 to 2 for dog or cat"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="Function should convert 28 to 3 for dog and 2 for cat"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Function should convert 100 to 21 for dog and 17 for cat"
            ),
        ]
    )
    def test_dof_and_cat_age(
            self,
            age_for_dog: int,
            age_for_cat: int,
            expected_age_dog_cat: list[int]
    ) -> None:
        assert get_human_age(age_for_dog, age_for_cat) == expected_age_dog_cat


class TestCatAndDogDataType:
    @pytest.mark.parametrize(
        "age_for_dog, age_for_cat, expected_exception", [
            pytest.param(
                0,
                "0",
                TypeError,
                id="You can use only 'int' type for age"
            ),
            pytest.param(
                0,
                [0],
                TypeError,
                id="You can use only 'int' type for age"
            ),
            pytest.param(
                0,
                {0},
                TypeError,
                id="You can use only 'int' type for age"
            ),
            pytest.param(
                0,
                (0,),
                TypeError,
                id="You can use only 'int' type for age"
            ),
        ]
    )
    def test_cat_and_dog_data_type(
            self,
            age_for_dog: int,
            age_for_cat: int,
            expected_exception: Exception,
    ) -> None:
        with pytest.raises(expected_exception):
            get_human_age(age_for_dog, age_for_cat)
