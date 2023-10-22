import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (27, 29, [2, 3]),

        pytest.param(
            0, 0,
            [0, 0],
            id="Аge cannot be equal to 0"
        ),

        pytest.param(
            -1, -100,
            [0, 0],
            id="Age must be positive"
        ),

        pytest.param(
            1000000,
            472,
            [249996, 91],
            id="Unreal age"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_test_get_human_age_correct_data_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat_age = 2", {"dog": 4})
