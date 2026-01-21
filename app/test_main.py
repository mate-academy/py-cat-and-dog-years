import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years,dog_years,expected_result",
        [
            pytest.param(
                -15,
                -15,
                [0, 0],
                id="should check negative age"
            ),

            pytest.param(
                0,
                0,
                [0, 0],
                id="should check age is 0"
            ),

            pytest.param(
                13.5,
                13.5,
                [0, 0],
                id="should check age, which not an integer"
            ),

            pytest.param(
                13,
                13,
                [0, 0],
                id="should check age less 15"
            ),

            pytest.param(
                24,
                24,
                [2, 2],
                id="should check age, which consist of 15 + 9"
            ),

            pytest.param(
                28,
                28,
                [3, 2],
                id="should check years, which include extra years"
            ),

            pytest.param(
                100,
                100,
                [21, 17],
                id="should check few extra years"
            )

        ]
    )
    def test_converting_to_human_age_correctly(
            self,
            cat_years: int,
            dog_years: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                "0",
                "0",
                id="when data is string"
            ),

            pytest.param(
                [0],
                [0],
                id="when data is list"
            ),

            pytest.param(
                {0},
                {0},
                id="when data is set"
            ),
        ]
    )
    def test_type_of_result(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
