import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            13,
            11,
            [0, 0],
            id="return zero if age less 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="return 1 if age equal 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="last year of 1 human year"
        ),
        pytest.param(
            25,
            26,
            [2, 2],
            id="add 1 after 24 years"
        ),
        pytest.param(
            0,
            29,
            [0, 3],
            id="dog years equal zero "
        ),
        pytest.param(
            28,
            0,
            [3, 0],
            id="cat years equal zero "
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="100 cat years should not be equal 100 dog`s`"
        ),
        pytest.param(
            -2,
            -1,
            [0, 0],
            id="negative age"
        ),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("abc", "re", id="str TypeError"),
        pytest.param([12], [1], id="list TypeError"),
    ]
)
def test_incorrect_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
