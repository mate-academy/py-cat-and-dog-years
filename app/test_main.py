import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "1",
                1,
                TypeError,
                id="should raise error when some age is not number"
            )
        ]
    )
    def test_raising_error_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return 0 human age when cat/dog 0...15"
            ),
            pytest.param(
                15,
                14,
                [1, 0],
                id="should return 1 human age for cat 0 for dog"
            ),
            pytest.param(
                14,
                15,
                [0, 1],
                id="should return 0 human age for cat 1 for dog"
            ),
            pytest.param(
                -1,
                -2,
                [0, 0],
                id="should work correctly with negative numbers"
            ),
            pytest.param(
                1000,
                2000,
                [246, 397],
                id="should work correctly with large numbers"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return 1 human age when cat/dog 15...24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return 2 human age when cat/dog 24...28/29"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return 21/17 when animal have extra human years"
            )
        ]
    )
    def test_count_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result
