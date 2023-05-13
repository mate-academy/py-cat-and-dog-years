import pytest
from app.main import get_human_age


class TestDifferentAges:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_value",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Function should work correct with when arguments = 0"
            ),
            pytest.param(
                0,
                15,
                [0, 1],
                id="Function should work correct if cat age is equal 0"
            ),

            pytest.param(
                15,
                0,
                [1, 0],
                id="Function should work correct if dog age is equal 0"
            ),

            pytest.param(
                -7,
                -5,
                [0, 0],
                id="Test should work correct with negative arguments"
            ),

            pytest.param(
                100,
                100,
                [21, 17],
                id="Test should work correct with normal arguments"
            ),

            pytest.param(
                28,
                28,
                [3, 2],
                id="Test should work correct with normal arguments"
            ),

            pytest.param(
                27,
                27,
                [2, 2],
                id="Test should work correct with normal arguments"
            )
        ])
    def test_different_ages(
            self,
            cat_age: int,
            dog_age: int,
            expected_value: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_value

    @pytest.mark.parametrize(
        "cat_age, dog_age, error",
        [
            pytest.param(
                "1",
                1,
                TypeError,
                id="Cat value should be int. Not string!"
            ),
            pytest.param(
                1,
                "1",
                TypeError,
                id="Dog value should be int. Not string!"
            ),

            pytest.param(
                [1],
                1,
                TypeError,
                id="Cat value should be int. Not list!"
            ),

            pytest.param(
                1,
                [1],
                TypeError,
                id="Dog value should be int. Not list!"
            ),
        ])
    def test_converting_animal_age_to_himan_expected_error(
            self,
            cat_age: int,
            dog_age: int,
            error: TypeError
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
