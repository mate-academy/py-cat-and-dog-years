import pytest
from app.main import get_human_age


class TestCatAndDogYears:
    @pytest.mark.parametrize(
        "animal_years,human_years",
        [
            pytest.param(
                (0, 0),
                [0, 0],
                id="the years of the dog and cat are equal to zero"
            ),
            pytest.param(
                (14, 14),
                [0, 0],
                id="the years of animals are equal to fourteen"
            ),
            pytest.param(
                (15, 15),
                [1, 1],
                id="the years of animals must equal one"
            ),
            pytest.param(
                (24, 24),
                [2, 2],
                id="the years of animals must equal two"
            ),
            pytest.param(
                (28, 28),
                [3, 2],
                id="difference in age of animals"
            ),
            pytest.param(
                (100, 100),
                [21, 17],
                id="100 human years"
            ),
            pytest.param(
                (27, 100),
                [2, 17],
                id="abudabu"
            ),
            pytest.param(
                (-1, -1),
                [0, 0],
                id="abudabu-2"
            ),
        ]
    )
    def test_general_function(
        self,
        animal_years: tuple,
        human_years: list
    ) -> None:
        animal_age = get_human_age(*animal_years)
        assert animal_age == human_years

    def test_empty_input(self) -> None:
        with pytest.raises(TypeError):
            get_human_age()

    def test_string_input(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(0, "string")
