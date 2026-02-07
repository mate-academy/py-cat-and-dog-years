import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, animal_age_in_human_years",
    [
        pytest.param(0, 0, [0, 0], id="0 years"),
        pytest.param(-1, -1, [0, 0], id="negative age"),
        pytest.param(14, 14, [0, 0], id="close to 15"),
        pytest.param(15, 15, [1, 1], id="one year"),
        pytest.param(23, 23, [1, 1], id="close to 24"),
        pytest.param(24, 24, [2, 2], id="two years"),
        pytest.param(27, 27, [2, 2], id="still two years"),
        pytest.param(28, 28, [3, 2], id="cat and dog years differ"),
        pytest.param(100, 100, [21, 17], id="high value")
    ]
)
def test_should_return(
        cat_age: int,
        dog_age: int,
        animal_age_in_human_years: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == animal_age_in_human_years
    ), (f"Cat age in human years should be {animal_age_in_human_years[0]}"
        f" and dog age should be {animal_age_in_human_years[1]}")


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param("hej", -1, TypeError, id="values should be integer"),
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
