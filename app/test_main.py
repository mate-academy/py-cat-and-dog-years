import pytest
from app.main import get_human_age


class TestMainModule:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Test [0, 0]"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Test [0, 0]"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="Test [1, 1]"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="Test [1, 1]"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="Test [2, 2]"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="Test [2, 2]"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="Test [3, 2]"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Test [21, 17]"
            ),
        ]
    )
    def test_module(self, cat_age: int, dog_age: int, result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result

    def test_module_error(self):
        with pytest.raises(TypeError):
            get_human_age("13", [13])

