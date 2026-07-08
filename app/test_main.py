import pytest

from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expect_list",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Check with zero parameters"),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Test with first boundary parameter 14"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="Boundary parameter 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="Boundary parameter 23"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="Boundary parameter 24"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="Boundary parameter cat-27, dog-28"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="Boundary parameter cat-28, dog-29"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Boundary parameter cat/dog=100"
            ),
            pytest.param(
                300,
                300,
                [71, 57],
                id="Big ages"
            )
        ]
    )
    def test_modify_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expect_list: list[int]
    ) -> None:

        assert get_human_age(cat_age, dog_age) == expect_list

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "",
                "-",
                TypeError,
                id="Raise TypeError if params are strings"
            ),
            pytest.param(
                2,
                -2,
                ValueError,
                id="Raise ValueError if age is negative number"
            ),
            pytest.param(
                500,
                500,
                ValueError,
                id="Raise ValueError if age is big number"
            ),
        ]
    )
    def test_raise_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: type[TypeError | ValueError]
    ) -> None:

        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
