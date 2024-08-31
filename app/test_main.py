from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "arguments,expected",
    [
        (
            (0, 0),
            [0, 0]
        ),
        (
            (14, 14),
            [0, 0]
        ),
        (
            (15, 15),
            [1, 1]
        ),
        (
            (23, 23),
            [1, 1]
        ),
        (
            (24, 24),
            [2, 2]
        ),
        (
            (27, 27),
            [2, 2]
        ),
        (
            (28, 28),
            [3, 2]
        ),
        (
            (100, 100),
            [21, 17]
        )

    ]
)
def test_the_output_has_to_be_equal_to_expected(
        arguments: tuple,
        expected: list[int]
) -> None:

    assert (get_human_age(arguments[0],
                          arguments[1])
            == expected)


def test_the_output_has_to_be_integer() -> None:
    with pytest.raises(TypeError):
        assert isinstance(get_human_age("Bob", 24)[1], int)
        assert isinstance(get_human_age("24", 24)[0], int)


def test_negative_or_large_numbers() -> None:
    assert get_human_age(-1, 2) == [0, 0]
