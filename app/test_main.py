import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_list",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="0 cat/dog years should convert into 0 human age."),
        pytest.param(
            14,
            14,
            [0, 0],
            id="14 cat/dog years should convert into 0 human age."),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 cat/dog years should convert into 1 human age."),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 cat/dog years should convert into 1 human age."),
        pytest.param(
            24,
            24,
            [2, 2],
            id="24 cat/dog years should convert into 2 human age."),
        pytest.param(
            27,
            28,
            [2, 2],
            id="27/28 cat/dog years should convert into 2 human age."),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28/29 cat/dog years should convert into 3 human age."),
        pytest.param(
            100,
            100,
            [21, 17],
            id="cat/dog years should convert considering each_year"),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age_list: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_list


def test_negative_ages() -> None:
    assert get_human_age(-2, 4) == [0, 0]
    assert get_human_age(15, -12) == [1, 0]


def test_large_ages() -> None:
    assert get_human_age(1000, 1000) == [246, 197]


def test_invalid_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("11", 10)
    with pytest.raises(TypeError):
        get_human_age(10, "26")
