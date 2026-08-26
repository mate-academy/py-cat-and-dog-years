import pytest

from app.main import get_human_age
from app.exception import InvalidParameter, InvalidParameterType


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return 0 if pets age is 0",
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return 0 if pets age is less than 15",
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return 1 if pets age is 15",
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return 1 if pets age is less than 24",
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return 2 if pets age is 24",
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should add 1 every 4 years for cats",
        ),
        pytest.param(
            32,
            32,
            [4, 3],
            id="should add 1 every 4 years for cats",
        ),
        pytest.param(
            29,
            29,
            [3, 3],
            id="should add 1 every 5 years for dogs",
        ),
        pytest.param(
            34,
            34,
            [4, 4],
            id="should add 1 every 5 years for dogs",
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should correctly calculate large pet ages",
        ),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, result",
    [
        pytest.param(14, [0, 0], id="cat age 14"),
        pytest.param(15, [1, 0], id="cat age 15"),
        pytest.param(23, [1, 0], id="cat age 23"),
        pytest.param(24, [2, 0], id="cat age 24"),
    ],
)
def test_cat_age_boundaries(cat_age: int, result: list) -> None:
    assert get_human_age(cat_age, 0) == result


@pytest.mark.parametrize(
    "dog_age, result",
    [
        pytest.param(14, [0, 0], id="dog age 14"),
        pytest.param(15, [0, 1], id="dog age 15"),
        pytest.param(23, [0, 1], id="dog age 23"),
        pytest.param(24, [0, 2], id="dog age 24"),
    ],
)
def test_dog_age_boundaries(dog_age: int, result: list) -> None:
    assert get_human_age(0, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(-1, 10, id="negative cat age"),
        pytest.param(10, -1, id="negative dog age"),
        pytest.param(-1, -1, id="both negative ages"),
    ]
)
def test_raise_exception(cat_age: int, dog_age: int) -> None:
    with pytest.raises(InvalidParameter):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("15", 15, id="string cat age"),
        pytest.param(15, "15", id="string dog age"),
        pytest.param(15.5, 15, id="float cat age"),
        pytest.param(15, 15.5, id="float dog age"),
        pytest.param(15, True, id="float dog age"),
        pytest.param(True, 15, id="float dog age"),
    ],
)
def test_raise_exception_for_invalid_datatype(
        cat_age: str | int | float | bool,
        dog_age: str | int | float | bool
) -> None:
    with pytest.raises(InvalidParameterType):
        get_human_age(cat_age, dog_age)
