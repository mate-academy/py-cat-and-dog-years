import pytest
from app.main import get_human_age


class TestChecksNumberAnswer:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(0, 0, [0, 0], id="if age equal zero"),
            pytest.param(14, 14, [0, 0], id="if age less one"),
            pytest.param(15, 15, [1, 1], id="if age equal one"),
            pytest.param(23, 23, [1, 1], id="if age more one"),
            pytest.param(24, 24, [2, 2], id="if age equal two"),
            pytest.param(27, 28, [2, 2], id="if age more two"),
            pytest.param(28, 29, [3, 3], id="if age equal three"),
            pytest.param(100, 100, [21, 17], id="if age big digits"),
            pytest.param(-3, -1, [0, 0], id="if age less zero")
        ]
    )
    def test_checks_number_answer(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age


def test_should_raise_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("3", 2.0)
