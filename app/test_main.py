import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [

            pytest.param(
                14,
                14,
                [0, 0],
                id="should calculate first year if < 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should calculate first year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should calculate second year"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should calculate third year differently"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should calculate realistic numbers of human age"
            ),
            pytest.param(
                456789456789,
                987653456776,
                [114197364193, 197530691352],
                id="should calculate unrealistic numbers of human age"
            ),
            pytest.param(
                -100,
                -100,
                [0, 0],
                id="should return 0 if input age is negative"
            ),
            pytest.param(
                0,
                20,
                [0, 1],
                id="should return 0 if input age is zero"
            ),
        ]
    )
    def test_with_different_data_sets(
            self,
            cat_age: int,
            dog_age: int,
            result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age,expected_error",
        [
            pytest.param(
                "cat_age",
                20,
                TypeError,
                id="should raise TypeError if input is not integer or float"
            ),


        ]
    )
    def test_correct_input_output_data_types(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_error: list
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(initial_cat_age, initial_dog_age)
