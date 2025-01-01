import pytest


from app.main import get_human_age


def test_correct_error_raised() -> None:
    with pytest.raises(TypeError):
        get_human_age(30, "30")


def test_output_not_changed_with_previous_value() -> None:
    get_human_age(100, 100)
    assert (
        get_human_age(28, 28) == [3, 2]
    ), "Previous values should not change current output"


@pytest.mark.parametrize(
    "cat_a, dog_a, result",
    [
        (-50, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3])
    ],
    ids=[
        "If age is less than 1 result should be 0",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age."
    ]
)
def test_get_human_age(cat_a: int, dog_a: int, result: list) -> None:
    assert (
        get_human_age(cat_a, dog_a) == result
    ), (f"Cat {cat_a} should convert to {result[0]},"
        f" dog {dog_a} should convert to {result[1]}")
