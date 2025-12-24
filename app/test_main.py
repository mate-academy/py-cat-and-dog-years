import pytest

from app.main import get_human_age


class TestsGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age_input, dog_age_input, expected_age",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return [0, 0]"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return [1, 1]"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return [1, 1]"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should return [21, 17]"
            ),
            pytest.param(
                -20, -20, [0, 0],
                id="should return [0, 0]"
            ),
            pytest.param(
                2000, 2000, [496, 397],
                id="should return [496, 397]"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="should return [2, 2]"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should return [3, 2]"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return [0, 0]"
            ),
        ]
    )
    def test_calculations(
            self,
            cat_age_input: int,
            dog_age_input: int,
            expected_age: list
    ) -> None:
        assert get_human_age(cat_age_input, dog_age_input) == expected_age

    def test_errors(
            self,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age("1", 1)
