import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            5, 6, [0, 0],
            id="return zero if age < 15 years"),
        pytest.param(
            23, 17, [1, 1],
            id="add 1 for 15 years"),
        pytest.param(
            26, 27, [2, 2],
            id="add 1 for 24 years"),
        pytest.param(
            28, 0, [3, 0],
            id="add 1 for next 4 cat years"),
        pytest.param(
            0, 29, [0, 3],
            id="add 1 for next 5 dog years"),
        pytest.param(
            -1, -2, [0, 0],
            id="return 0 for negative value of age"),
        pytest.param(
            100,
            100,
            [21, 17],
            id="return different values if cat_age = dog_age"),
    ]
)
def test_convert_human_age(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(
            "20", "40",
            id="should raise error if value type is string"
        ),
        pytest.param(
            {20}, {40},
            id="should raise error if value type is dict"
        ),
        pytest.param(
            [20], [40],
            id="should raise error if value type is list"
        ),
        pytest.param(
            (20, 10), (40, 50),
            id="should raise error if value type is tuple"
        ),

    ]
)
def test_convert_human_age_with_wrong_type_age(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
