import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return [0, 0]"
            ),
            pytest.param(
                1, 1, [0, 0],
                id="should return [0, 0]"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return [0, 0]"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return [1, 1]"
            ),
            pytest.param(
                24, 23, [2, 1],
                id="should return [2, 1]"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should return [3, 2]"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should return [21, 17]"
            )
        ]
    )
    def test_is_correct_result(
            self,
            cat_age,
            dog_age,
            expected
    ):
        assert get_human_age(cat_age, dog_age) == expected


def test_if_input_is_correct():
    with pytest.raises(TypeError):
        get_human_age("-1", [])