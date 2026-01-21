import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "animal_ages,human_ages",
        [
            ((0, 0), [0, 0]),
            ((14, 14), [0, 0]),
            ((15, 15), [1, 1]),
            ((23, 23), [1, 1]),
            ((24, 24), [2, 2]),
            ((27, 27), [2, 2]),
            ((27, 28), [2, 2]),
            ((28, 27), [3, 2]),
            ((100, 100), [21, 17]),
            ((1500, 2700), [371, 537]),
            ((1500, 2700), [371, 537]),
            ((-3, 2), [0, 0]),
            ((3, -7), [0, 0]),
            ((-128833, -2), [0, 0]),
        ]
    )
    def test_expected_values_are_correct(
        self,
        animal_ages: tuple,
        human_ages: list[int]
    ) -> None:
        result = get_human_age(*animal_ages)
        assert result == human_ages


class TestErrorCases:
    @pytest.mark.parametrize(
        "animal_ages",
        [
            (0, "string"),
            (2, [1, 3])
        ]
    )
    def test_error_case(self, animal_ages: tuple) -> None:
        with pytest.raises(TypeError):
            get_human_age(*animal_ages)
