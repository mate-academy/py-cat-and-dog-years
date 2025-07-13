import pytest
import app.main as main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(cat_age: int,
                                dog_age: int, expected: list[int]) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


def test_return_type_and_length() -> None:
    result = main.get_human_age(10, 20)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
