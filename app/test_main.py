import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, result", [(0, 0, [0, 0]),
                                                      (14, 14, [0, 0]),
                                                      (15, 15, [1, 1]),
                                                      (23, 23, [1, 1]),
                                                      (24, 24, [2, 2]),
                                                      (27, 27, [2, 2]),
                                                      (28, 28, [3, 2]),
                                                      (100, 100, [21, 17])])
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result, \
        f"Human ages should be {result}."


def test_result_should_be_two_integers() -> None:
    result = get_human_age(22, 22)
    assert isinstance(result[0], int) and isinstance(result[1], int), \
        "Results should be two integers."


def test_should_be_zero_when_less_then_fifteen() -> None:
    result = get_human_age(13, 12)
    assert result == [0, 0], "Result should be 0 when less than fifteen."


def test_should_return_diff_human_age() -> None:
    result = get_human_age(28, 28)
    assert result[0] != result[1], "Human ages should be different."
