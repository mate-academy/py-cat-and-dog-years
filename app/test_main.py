import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "animal_age,expected",
    [
        pytest.param(
            [0, 0],
            [0, 0],
            id="should expected return when age animal equal zero"
        ),
        pytest.param(
            [15, 15],
            [1, 1],
            id="should expected return when the animals one human year old"
        ),
        pytest.param(
            [24, 24],
            [2, 2],
            id="should expected return when the animals two human year old"
        ),
        pytest.param(
            [28, 28],
            [3, 2],
            id="should expected return when the years are different"
        ),
    ]
)
def test_should_return_excepted_result(
        animal_age,
        expected
):
    result = get_human_age(animal_age[0],animal_age[1])

    assert result == expected
