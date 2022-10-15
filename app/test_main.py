import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_array",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should return [0, 0] for cat and dog with age 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should return [0, 0] for cat and dog with age < 15"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should return [1, 1] for cat and dog with age equal to 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should return [1, 1] for cat and dog with age equal to 23"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="should return [2, 2] for cat and dog with age equal to 24"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="should return [2, 2] for cat and dog with age 27"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="should return [3, 2] for cat and dog with age 28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should return [21, 17] for cat and dog with age 100"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_array: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_array
