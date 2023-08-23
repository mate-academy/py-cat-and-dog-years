import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                -3, -3, [0, 0], id="negative age should give list with zeros"
            ),
            pytest.param(
                0, 0, [0, 0], id="zero age should give list with zeros"
            ),
            pytest.param(
                1200, 1200, [296, 237], id="big ages"
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
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    def test_correct_param(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("8", 8)
