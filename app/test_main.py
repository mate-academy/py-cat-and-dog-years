import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="test should return [0, 0] when ages are 0"
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="test should return [0, 0] when ages are negative"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="test should return [21, 17] when ages are 100"
        ),
    ],
)
def test_calculates_ages_correctly(cat_age: int,
                                   dog_age: int,
                                   expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(
            "two",
            [1, 2, 3]
        )
    ]
)
def test_raises_type_error_correctly(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
