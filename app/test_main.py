import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2])
    ],
    ids=[
        "Human age should be [0, 0] if cat/dog years is [0, 0]",
        "Human age should be [0, 0] if cat/dog years is [14, 14]",
        "Human age should be [1, 1] if cat/dog years is [15, 15]",
        "Human age should be [2, 2] if cat/dog years is [27, 27]",
        "Human age should be [3, 2] if cat/dog years is [28, 28]"
    ]
)
def test_should_correctly_convert_years(cat_age: int,
                                        dog_age: int,
                                        result: int) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_should_raise_error_if_any_input_missing_or_not_valid() -> None:
    with pytest.raises(TypeError):
        get_human_age("2", [4])
