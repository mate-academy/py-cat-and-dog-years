import pytest

from app.main import get_human_age


class TestConvert:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
            (-1, -1, [0, 0])
        ]
    )
    def test_must_return_expected_result(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result


def test_not_integer_type_exception() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", 1)
