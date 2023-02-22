import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat, dog, result",
        [
            pytest.param(
                -1, -2,
                [0, 0],
                id="test not positive human age"
            ),
            pytest.param(
                0, 0,
                [0, 0],
                id="test zero human age"
            ),
            pytest.param(
                10, 14,
                [0, 0],
                id="test less than one human age"
            ),
            pytest.param(
                15, 16,
                [1, 1],
                id="test one human age"
            ),
            pytest.param(
                25, 26,
                [2, 2],
                id="test two human age"
            ),
            pytest.param(
                18, 28,
                [1, 2],
                id="test different human age"
            ),
            pytest.param(
                100, 100,
                [21, 17],
                id="test should return expected years"
            ),
        ]
    )
    def test_modify_correctly(self, cat: int, dog: int, result: list) -> None:
        assert get_human_age(cat, dog) == result


def test_input_correctly() -> None:
    with pytest.raises(TypeError):
        get_human_age("3", [8])
