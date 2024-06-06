import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should return 0 when dog/cat years are 0"
        ),
        pytest.param(
            13, 14, [0, 0],
            id="should return 0 when dog/cat years less 15"
        ),
        pytest.param(
            15, 23, [1, 1],
            id="should return 1 when age between 15 and 23"
        ),
        pytest.param(
            24, 27, [2, 2],
            id="should return 2 when age between 24 and 28"
        ),
        pytest.param(
            29, 17, [3, 1],
            id="return 1 when age between 15 and 23"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="100 human years should be 21 and 17 years for dog and cat"
        )
    ]
)
def test_get_human_age_from_animals(cat_age: int,
                                    dog_age: int,
                                    human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("25", 0, id="age must be int"),
        pytest.param(15, "0", id="age must be int"),
        pytest.param({1: 2}, [], id="age must be int")
    ]
)
def test_get_human_age_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
