import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="check zeros when zero ages"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="check zeros when no zero ages"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="check human year - 1, when years are 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="check human year - 1, when years are 23"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="check human year - 2, when years are 24"
        ),
        pytest.param(
            28,
            24,
            [3, 2],
            id="check correct cat - human years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="check correct 100 years"
        ),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(
            "0",
            0,
            [0, 0],
            id="check error when cat years is str"
        ),
        pytest.param(
            14,
            "14",
            [0, 0],
            id="check error when dog years is str"
        ),
    ]
)
def test_error_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[[int]]
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
