from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(0, 0, [0, 0],
                         id="should return zero when age is equal zero"),
            pytest.param(14, 14, [0, 0],
                         id="should return 0 "
                            "when age is less than first year"),
            pytest.param(15, 15, [1, 1],
                         id="should return 1 if animal age "
                            "is equal to first year"),
            pytest.param(23, 23, [1, 1],
                         id="should return 1 "
                            "if animal age less than sum of two years"),
            pytest.param(24, 24, [2, 2],
                         id="should return 2 if animal age "
                            "is equal to sum of two years"),
            pytest.param(27, 27, [2, 2],
                         id="should add 2 to when animal age - years is 0"),
            pytest.param(28, 28, [3, 2],
                         id="should return different resuld for dog and cat"),
            pytest.param(100, 100, [21, 17],
                         id="should return correct result with huge numbers"),
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected


def test_get_error_if_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age(1, "1")
