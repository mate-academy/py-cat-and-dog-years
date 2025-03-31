import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="test zero human age when cat and dog ages is 0"
        ),
        pytest.param(
            1,
            1,
            [0, 0],
            id="test zeros when cat and dog ages is 1"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="test zeros when cat and dog ages is 14"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="test human age 1 for animal age 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="test human age 1 for animal ages 23"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test human age 2 for animal ages 24"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="test different human ages when animal ages is the same"
        ),
        pytest.param(
            29,
            29,
            [3, 3],
            id="test different human ages when animal ages is the same"
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="test negative values in animal ages"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="test large values is animal ages"
        ),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_wrong_data_should_raise_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", 1)
