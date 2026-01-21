import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should work with zero ages"),
            pytest.param(
                14, 14, [0, 0],
                id="should work with ages less than first 15 animal years"),
            pytest.param(
                15, 15, [1, 1],
                id="should work with ages equal to first 15 animal years"),
            pytest.param(
                23, 23, [1, 1],
                id="should work with ages less than 24"),
            pytest.param(
                24, 24, [2, 2],
                id="should work with ages equal to 24"),
            pytest.param(
                27, 27, [2, 2],
                id="should work with cat age is less than 28"),
            pytest.param(
                28, 28, [3, 2],
                id="should work with dog age less than 29, "
                   "cat age is equal to 28"),
            pytest.param(
                29, 29, [3, 3],
                id="should work with dog age equal to 29"),
            pytest.param(
                2537, 9131, [630, 1823],
                id="should work with large numbers ages"),
            pytest.param(
                -37, -31, [0, 0],
                id="should work with negative numbers ages"),
            pytest.param(
                37.3, 31.9, [5, 3],
                id="should work with float numbers ages"),
        ]
    )
    def test_return_valid_result(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                "13", "12",
                id="should raise an error when both arguments aren't numbers"),
            pytest.param(
                3, "25",
                id="should raise an error when dog age is not a number"),
            pytest.param(
                "28", 19,
                id="should raise an error when cat age is not a number")
        ]
    )
    def test_should_raise_error_if_incorrect_type(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
