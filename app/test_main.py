import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(-5, -1, [0, 0], id="negative ages return 0"),
        pytest.param(0, 0, [0, 0], id="0 years return 0"),
        pytest.param(14, 14, [0, 0], id="14 years still return 0"),
        pytest.param(15, 15, [1, 1], id="15 years return 1"),
        pytest.param(23, 23, [1, 1], id="23 years still return 1"),
        pytest.param(24, 24, [2, 2], id="24 years return 2"),
        pytest.param(27, 28, [2, 2], id="cat 27 / dog 28 still return 2"),
        pytest.param(28, 29, [3, 3], id="cat 28 / dog 29 return 3"),
        pytest.param(100, 100, [21, 17], id="large ages convert correctly"),
    ]
)
def test_should_convert_animal_age_to_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("15", 15, id="string cat age raises TypeError"),
        pytest.param(15, None, id="None dog age raises TypeError"),
    ]
)
def test_should_raise_type_error_for_invalid_age_type(
        cat_age: object,
        dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
