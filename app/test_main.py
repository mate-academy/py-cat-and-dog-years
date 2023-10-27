import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_ages",
        [
            pytest.param(
                10,
                10,
                [0, 0],
                id="get zeros when ages are under 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="test when ages are equal 15"
            ),
            pytest.param(
                23,
                17,
                [1, 1],
                id="test when ages are between 15 and 24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="test when ages are equal 24"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="test when ages are equal 28"
            ),
            pytest.param(
                44,
                44,
                [7, 6],
                id="test if function works for third+ year"
            ),
        ]
    )
    def test_get_correct_answers(
            self,
            cat_age: int,
            dog_age: int,
            expected_ages: list[int]
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected_ages

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                0, 0, ValueError,
                id="Throws error if ages are equal to zero"
            ),
            pytest.param(
                -1, 6, ValueError,
                id="Throws error if one of ages is negative"
            ),
            pytest.param(
                100, 5, ValueError,
                id="Throws error if one of ages is higher than 99"
            ),
            pytest.param(
                1.6, "6.0", TypeError,
                id="Throws error if one of ages isn't integer"
            ),
        ]
    )
    def test_if_function_throws_errors(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
