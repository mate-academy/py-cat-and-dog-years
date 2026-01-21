import pytest

from app.main import get_human_age


def test_should_return_array() -> None:
    assert type(get_human_age(5, 5)) == list


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            14, 14, [0, 0], id="return zero if age less fifteen"
        ),
        pytest.param(
            15, 23, [1, 1], id="return one if age between 15 and 23"
        ),
        pytest.param(
            27, 28, [2, 2], id="if age more 23 adds one year"
                               " every 4 years for a cat and 5 years for a dog"
        )
    ]
)
def test_should_return_age_in_human_years(
        cat_age: int,
        dog_age: int,
        result: int
) -> None:
    assert get_human_age(cat_age, dog_age) == result
