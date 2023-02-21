import pytest
from app.main import get_human_age


class TestChecksNumberAnswer:

    @pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
            (-3, -1, [0, 0])
        ]
    )


    def test_checks_number_answer(self, cat_age, dog_age, human_age):
        assert get_human_age(cat_age, dog_age) == human_age

    # def test_if_age_equal_zero(self) -> None:
    #     assert get_human_age(0, 0) == [0, 0]
    #
    # def test_if_age_less_one(self) -> None:
    #     assert get_human_age(14, 14) == [0, 0]
    #
    # def test_if_age_equal_one(self) -> None:
    #     assert get_human_age(15, 15) == [1, 1]
    #
    # def test_if_age_more_one(self) -> None:
    #     assert get_human_age(23, 23) == [1, 1]
    #
    # def test_if_age_equal_two(self) -> None:
    #     assert get_human_age(24, 24) == [2, 2]
    #
    # def test_if_age_more_two(self) -> None:
    #     assert get_human_age(27, 28) == [2, 2]
    #
    # def test_if_age_equal_three(self) -> None:
    #     assert get_human_age(28, 29) == [3, 3]
    #
    # def test_if_age_big_digits(self) -> None:
    #     assert get_human_age(100, 100) == [21, 17]
    #
    # def test_if_age_big_digits(self) -> None:
    #     assert get_human_age(-3, -1) == [0, 0]


def test_should_raise_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("3", 2.0)