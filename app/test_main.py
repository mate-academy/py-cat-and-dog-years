import pytest

from app.main import get_human_age


class TestCorrectInputs:
    @pytest.mark.parametrize(
        "cat,dog,result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17])
        ]
    )
    def test_correct_outputs(self, cat: int,
                             dog: int, result: list[int]) -> None:
        assert (get_human_age(cat, dog) == result)


class TestIncorrectInputs:
    @pytest.mark.parametrize(
        "cat,dog",
        [
            (-1, 0),
            (0, -5),
            (-1, -7)
        ]
    )
    def test_invalid_input_negative(self, cat: int, dog: int) -> None:
        with pytest.raises(ValueError):
            get_human_age(cat, dog)

    @pytest.mark.parametrize(
        "cat,dog",
        [
            (1.5, 2),  # float
            ("3", 4),  # string
            (None, 1),  # None
            ([1], 2),  # lista
            ({"cat": 2}, 5)  # dict
        ]
    )
    def test_invalid_input_types(self, cat: all, dog: all) -> None:
        with pytest.raises((TypeError, ValueError)):
            get_human_age(cat, dog)
