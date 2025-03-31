import pytest

from app.main import get_human_age, convert_to_human


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "input_cats, input_dogs, expected_result",
        [
            pytest.param(
                15.3,
                22.9,
                [1, 1],
                id="should return correct list if "
                   "float in input: cat=15.3, dog=22.9"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return correct list if cat and dog input: 14"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return correct list if cat and dog input: 23"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return correct list if cat and dog input: 28"
            )
        ]
    )
    def test_correct_results(
            self,
            input_cats: int,
            input_dogs: int,
            expected_result: list[int]
    ) -> None:

        result = get_human_age(input_cats, input_dogs)
        assert result == expected_result


class TestConvertToHuman:
    def test_should_also_take_float_as_argument(self) -> None:
        result = convert_to_human(17, 15, 9.4, 4.2)
        assert result == 1
