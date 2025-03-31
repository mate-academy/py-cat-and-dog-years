import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return [0, 0] when ages equal zero"
            ),
            pytest.param(
                -1, -2, [0, 0],
                id="should return [0, 0] when ages are not correct"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return [0, 0] when ages less than 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return [1, 1] for first 15 animal years"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return [2, 2] for next 9 animal (after age of 15)"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="every 4 next cat years give 1 extra human year"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="every 5 next dog years give 1 extra human year"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="test should return expected result"
            )
        ]
    )
    def test_return_expected_result(self,
                                    cat_age: int,
                                    dog_age: int,
                                    expected_result: list
                                    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result


def test_raise_error_for_incorrect_data_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("2", 3.0)
