import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="human age should be zero if animals are zero"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="human age should be zero if animals are under fifteen"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="human age should be one if animals are under twenty four"
            ),
            pytest.param(
                44,
                44,
                [7, 6],
                id="should work for different years"
            ),
            pytest.param(
                144,
                744,
                [32, 146],
                id="should work for different big integer"
            ),
            pytest.param(
                -41,
                -3,
                [0, 0],
                id="if animal's age less zero"
            )
        ]
    )
    def test_for_borderline_cases(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,error",
        [
            pytest.param(
                73,
                "tetraboraks",
                TypeError,
                id="should be TypeError"
            )
        ]
    )
    def test_type_error(
            self,
            cat_age: int,
            dog_age: int,
            error: Exception
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
