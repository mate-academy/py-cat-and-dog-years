import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should return 0 when years are 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should return 0 when years are 14"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should return 1 when years are 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should return 1 when years are 23"),
        pytest.param(
            24, 24, [2, 2],
            id="should return 2 when years are 24"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="should return 2 when years are 27"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="should return 3 and 2 when years equal 28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should return 21 and 17 when years equal 100"
        ),
        pytest.param(
            -1, 1000, [0, 0],
            id="return 0, 0 when cat_age is less than 0"
        ),
        pytest.param(
            1000, -1, [0, 0],
            id="return 0, 0 when dog_age is less than 0"
        ),
        pytest.param(
            1001, 1000, [0, 0],
            id="return 0, 0 when cat_age is greater than 1000"
        ),
        pytest.param(
            1000, 1001, [0, 0],
            id="return 0, 0 when dog_age is greater than 1000"
        ),
    ]
)
def test_cat_and_dog_age(
        cat_age: int,
        dog_age: int ,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("100", 100),
        (100, "100"),
        ("100", "100"),
        (100.1, 100),
        (100, 100.1),
    ]
)
def test_should_raise_type_error_when_values_are_not_integers(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
