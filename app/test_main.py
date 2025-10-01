from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(-1, -5, [0, 0], id="(-1, -5)->[0, 0]"),
            pytest.param(14, 14, [0, 0], id="(14, 14)->[0, 0]"),
            pytest.param(15, 15, [1, 1], id="(15, 15)->[1, 1]"),
            pytest.param(23, 23, [1, 1], id="(23, 23)->[1, 1]"),
            pytest.param(24, 24, [2, 2], id="(24, 24)->[2, 2]"),
            pytest.param(28, 28, [3, 2], id="(28, 28)->[3, 2]"),
            pytest.param(29, 29, [3, 3], id="(29, 29)->[3, 3]"),
            pytest.param(100, 100, [21, 17], id="(100, 100)->[21, 17]"),
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

    def check_is_list(self) -> None:
        assert isinstance(get_human_age(28, 28), list)

    def chec_len_list(self) -> None:
        assert len(get_human_age(28, 28)) == 2

    with pytest.raises(TypeError):
        get_human_age(None, "28")