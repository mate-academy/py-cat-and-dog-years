from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(0, 14, [0, 0]),
            pytest.param(23, 0, [1, 0]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(28, 29, [3, 3]),
            pytest.param(100, 100, [21, 17]),
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected: list
                           ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    def test_check_integer(self) -> None:
        assert all(isinstance(x, int) for x in get_human_age(28, 28))
