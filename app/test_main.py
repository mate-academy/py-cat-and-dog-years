import pytest

from app.main import get_human_age


class TestConvertToHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                -1, -2, [0, 0], id="negative age values give zero in result"
            ),
            pytest.param(
                0, 0, [0, 0], id="zero age values give zero in result"
            ),
            pytest.param(
                120, 120, [26, 21], id="test wih big age values"
            ),
            pytest.param(
                14, 14, [0, 0], id="pet's age is less than 1 human's year"
            ),
            pytest.param(
                15, 15, [1, 1], id="15 pet years equals 1 human year"
            ),
            pytest.param(
                23, 23, [1, 1], id="pet's age is less than 2 human's years"
            ),
            pytest.param(
                24, 24, [2, 2], id="24 pet years equals 2 human years"
            ),
            pytest.param(
                29, 29, [3, 3], id="29 pet years equals 3 human years"
            ),
        ],
    )
    def test_get_human_age(
            self, cat_age: int, dog_age: int, result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    def test_for_correct_parameters(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("2", 1)
