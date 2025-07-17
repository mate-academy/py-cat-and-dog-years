import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
    14, 14, [0, 0],
            id="zero years"
        ),
        pytest.param(
    15, 15, [1, 1],
            id="1 year"
        ),
        pytest.param(
    23, 23, [1, 1],
            id="1 year"
        ),
        pytest.param(
    24, 24, [2, 2],
            id="2 years"
        ),
        pytest.param(
    27, 27, [2, 2],
            id="2 years"
        ),
        pytest.param(
    28, 28, [3, 2],
            id="3 to 2 years"
        ),
        pytest.param(
    100, 100, [21, 17],
            id="21 to 17 years"
        ),
    ]
)

def test_cat_dog_age_to_human_age(
    cat_age,
    dog_age,
    human_age
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age