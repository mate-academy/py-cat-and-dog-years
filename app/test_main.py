import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return list with zero ages"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return list with zero ages"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="cat and dog ages should equal 1 human year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="cat and dog ages should equal 1 human year"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="cat and dog ages should equal 2 human years"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="cat and dog ages should equal 2 human years"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="cat and dog ages should equal 3 and 2 human years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="cat and dog ages should equal 21 and 17 human years"
        )
    ]
)
def test_get_human_age(
    cat_age,
    dog_age,
    expected_age
):
    assert get_human_age(cat_age, dog_age) == expected_age
