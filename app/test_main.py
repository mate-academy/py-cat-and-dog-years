import pytest
from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,ages",
        [
            pytest.param(
                0, 0, [0, 0],
                id="age is zero"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="less than 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="age equals 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="age has not reached first_year + second_year"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="age has reached first_year + second_year"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="age less than 28"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="age equals 28"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="age is a big number"
            ),
        ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            ages: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == ages

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                "ten", 10,
                id="cat_age is a string"
            ),

            pytest.param(
                10, "ten",
                id="dog_age is a string"
            ),

            pytest.param(
                None, 10,
                id="cat_age is None"
            ),

            pytest.param(
                10, None,
                id="dog_age is None"
            ),

            pytest.param(
                [10], 10,
                id="cat_age is a list"
            ),

            pytest.param(
                10, [10],
                id="dog_age is a list"
            ),

            pytest.param(
                {"age": 10}, 10,
                id="cat_age is a dict"
            ),

            pytest.param(
                10, {"age": 10},
                id="dog_age is a dict"
            ),
        ]
    )
    def test_get_human_age_incorrect_types(self,
                                           cat_age: int,
                                           dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
