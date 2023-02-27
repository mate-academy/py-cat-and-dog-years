import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_years",
    [
        pytest.param(
            -1, 8, [0, 0],
            id="should return 0, 0"
        ),
        pytest.param(
            2, -10, [0, 0],
            id="should return 0, 0"
        ),
        pytest.param(
            -2, -25, [0, 0],
            id="should return 0, 0"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="should return 0, 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should return 0, 0"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should return 1, 1"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should return 1, 1"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="should return 2, 2"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="should return 2, 2"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="should return 3, 2"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should return 21, 17"
        ),
        pytest.param(
            1.2, 8.5, [0, 0],
            id="should return 0, 0"
        ),
        pytest.param(
            15.1, 16.1, [1, 1],
            id="should return 0, 0"
        ),
        pytest.param(
            24.9, 25.6, [2, 2],
            id="should return 2, 2"
        ),
        pytest.param(
            28.1, 28.1, [3, 2],
            id="should return 3, 2"
        ),
        pytest.param(
            100.3, 100.3, [21, 17],
            id="should return 21, 17"
        )
    ]
)
def test_get_correct_human_age(cat_age: (int, float),
                               dog_age: (int, float),
                               expected_years: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_years


def test_typeerror_when_not_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "25")
