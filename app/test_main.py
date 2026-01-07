import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "age_cat, age_dog, expected",
    [
        pytest.param(
            0, 0, [0, 0], id="expected 0 when cat and dog age are 0"
        ),
        pytest.param(
            14, 14, [0, 0], id="should give 0 human year after 14 cat/dog year"
        ),
        pytest.param(
            15, 15, [1, 1], id="should give 1 human year after 15 cat/dog year"
        ),
        pytest.param(
            23, 23, [1, 1], id="should give 1 human year after 23 cat/dog year"
        ),
        pytest.param(
            24, 24, [2, 2], id="should give 2 human year after 24 cat/dog year"
        ),
        pytest.param(
            28, 28, [3, 2], id="should give 3/2 human years 28/28 cat/dog year"
        ),
        pytest.param(
            28, 29, [3, 3], id="should give 3 human years 28/29 cat/dog year"
        ),
        pytest.param(
            100, 100, [21, 17], id="chek wright count for cat/dog year"
        ),
        pytest.param(
            -5, -10, [0, 0], id="expected 0 when cat and dog age are negative"
        ),
    ]
)
def test_should_return_zeros(
        age_cat: int,
        age_dog: int,
        expected: list
) -> None:
    assert get_human_age(age_cat, age_dog) == expected


@pytest.mark.parametrize(
    "age_cat, age_dog, expected",
    [
        pytest.param(
            "100",
            True,
            TypeError,
            id="should raise TypeError when age category is invalid"
        )
    ]
)
def test_raises_errors(
        age_cat: int,
        age_dog: int,
        expected: type
) -> None:
    with pytest.raises(expected):
        get_human_age(age_cat, age_dog)
