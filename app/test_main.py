import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,list_human_ages",
    [
        pytest.param(0, 0, [0, 0], id="Check zero values"),
        pytest.param(14, 14, [0, 0], id="Zero human age"),
        pytest.param(15,
                     15,
                     [1, 1],
                     id="Minimum pet's years for the first human age"),
        pytest.param(23, 23, [1, 1], id="The first human age"),
        pytest.param(24,
                     24,
                     [2, 2],
                     id="Minimum pet's years for the second human age"),
        pytest.param(27, 27, [2, 2], id="The second human age"),
        pytest.param(28, 28, [3, 2], id="The third human age for cat"),
        pytest.param(100,
                     100,
                     [21, 17],
                     id="Human ages for  100-year-old cats and dogs"),

    ]
)
def test_human_years(cat_age: int,
                     dog_age: int,
                     list_human_ages: list) -> None:
    assert get_human_age(cat_age, dog_age) == list_human_ages


@pytest.mark.parametrize(
    "cats_age,dogs_age",
    [
        pytest.param("3", "2"),
        pytest.param([15], 2),
    ]
)
def test_type_err_exceptions(cats_age: int, dogs_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cats_age, dogs_age)
